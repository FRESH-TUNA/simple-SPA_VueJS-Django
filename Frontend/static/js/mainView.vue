var postTemplate = {
  template:
  `
    <div>
      야옹
    </div>
  `
}

var detailTemplate = {
  template:
  `
    <div>
      멍멍
    </div>
  `
}

var mainTemplate = {
  data: function() {
    return {
      elements: [
        {
            id:1,
            date:2,
            title:'hoho',
            content: '안녕하세요'
        },
        {
            id:2,
            date:3,
            title:'hihi',
            content: '안녕하세요'
        },
        {
            id:2,
            date:3,
            title:'hihi',
            content: '안녕하세요'
        },
        {
            id:2,
            date:3,
            title:'hihi',
            content: '안녕하세요'
        }
      ],
      postsStyleObject: {
        padding: '5%',
      },
      postStyleObject: {
        width: '100%',
        border: '1px solid black',
        'margin-top': '10px'
      }
    }
  },
  template:
  `
    <div v-bind:style="postsStyleObject">
      <div v-for="element in elements" :element="element" :key="element.id" v-bind:style="postStyleObject">
        <h3>{{element.title}}</h3>
        <div>{{element.content}}</div>
        <a>{{element.date}}</a>
        
        <button class="btn btn-primary">update</button>
        <button class="btn btn-primary">delete</button>
      </div>
    </div>
  `
}

var mainview = new Vue({
    el: '#mainView',
    data: {
        elements: [
            {
                id:1,
                date:2,
                title:'hoho'
            },
            {
                id:2,
                date:3,
                title:'hihi'
            },
            {
                id:2,
                date:3,
                title:'hihi'
            },
            {
                id:2,
                date:3,
                title:'hihi'
            }
        ],
        currentView: 'main-template'
    },
    components: {
      'main-template':mainTemplate,
      'post-template':postTemplate,
      'detail-template':detailTemplate
    }
});
