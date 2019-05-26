axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"


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
      'main-template':httpVueLoader('/static/js/mainTemplate.vue'),
      'create-template':httpVueLoader('/static/js/createTemplate.vue'),
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
        axios.get('http://127.0.0.1:8000/api/' + id + '/delete')
          .then(response => (this.readPosts())
        );
      }
    },
    created() {
      this.readPosts()
    }
});
