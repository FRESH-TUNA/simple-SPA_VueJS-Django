axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

var postTemplate = {
  template:
  `
    <div>
      야옹
    </div>
  `
}

var createTemplate = {
  props: ['currentViewData'],
  data: function() {
    return {
      textareaStyleObject: {
        height: '300px'
      }
    }
  },
  template:
  `
    <form>
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" placeholder="Enter title" v-model:value="currentViewData.title">
      </div>
      <div class="form-group">
        <label for="content">Content</label>
        <textarea class="form-control" :style="textareaStyleObject" v-model:value="currentViewData.content"></textarea>
      </div>
      <button type="button" class="btn btn-primary" @click="mainview.createPost(currentViewData.title,currentViewData.content,currentViewData.id)">Submit</button>
    </form>
  `
}

var mainTemplate = {
  props: ['currentViewData'],
  data: function() {
    return {
      postStyleObject: {
        width: '100%',
        border: '1px solid black',
        'margin-top': '10px'
      },
      postTitleStyleObject: {
        display: 'flex',
        'justify-content': 'space-between'
      },
      postButtonsStyleObject: {
        display: 'flex',
        'flex-direction': 'row-reverse'
      }
    }
  },
  template:
  `
    <div>
      <div v-for="element in currentViewData" :element="element" :key="element.id" v-bind:style="postStyleObject">
        <div v-bind:style="postTitleStyleObject">
          <h3>{{element.title}}</h3>
          <a>{{element.published_date}}</a>
        </div>
        <div>{{element.content}}</div>
        <div v-bind:style="postButtonsStyleObject">
          <button class="btn btn-primary" @click="mainview.showUpdateForm(element.id)">update</button>
          <button class="btn btn-primary" @click="mainview.deletePost(element.id)">delete</button>
        </div>
      </div>
    </div>
  `
}

var mainview = new Vue({
    el: '#mainView',
    data: {
        currentViewData: [],
        postsStyleObject: {
          padding: '5%',
        },
        currentView: 'main-template'
    },
    components: {
      'main-template':mainTemplate,
      'create-template':createTemplate,
    },
    methods: {
      readPosts: function() {
        axios.get('http://127.0.0.1:8000/api/')
          .then(response => {
              this.currentViewData = response.data.posts
              this.currentView = 'main-template'
          });
      },
      createPost: function(_title, _content, id) {
          csrftoken = Cookies.get('csrftoken'); // Using JS Cookies library
          if(id == undefined) {
            axios.post('http://127.0.0.1:8000/api/create', 
            {
              headers: {X_CSRFTOKEN: csrftoken}, 
              title : _title, 
              content: _content
            }).then(response => {
              this.readPosts()
              this.currentView = 'main-template'
            })
          }
          else {
            axios.post('http://127.0.0.1:8000/api/' + id + '/update', 
            {
              headers: {X_CSRFTOKEN: csrftoken}, 
              title : _title, 
              content: _content
            }).then(() => {
              this.readPosts()
              this.currentView = 'main-template'
            })
          }
      },
      showUpdateForm: function(id) {
        this.currentView = 'create-template'
        axios.get('http://127.0.0.1:8000/api/' + id)
          .then(response => (this.currentViewData = response.data.post)
        );
      },
      deletePost: function(id) {

      }
    },
    created() {
      this.readPosts()
    }
});
