var postTemplate = {
  template:
  `
    <div>
      야옹
    </div>
  `
}

var createTemplate = {
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
        <input type="text" class="form-control" placeholder="Enter title">
      </div>
      <div class="form-group">
        <label for="content">Content</label>
        <textarea class="form-control" v-bind:style="textareaStyleObject"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
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
          <button class="btn btn-primary">update</button>
          <button class="btn btn-primary">delete</button>
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
          .then(function(response){
            mainview.currentViewData = response.data.posts; // 객체 형태로 반환. 파싱작업 불필
          });
      }
    },
    created() {
      this.readPosts()
    }
});
