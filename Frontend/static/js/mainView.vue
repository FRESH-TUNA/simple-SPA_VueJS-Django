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
  /*
  props: {
    elements: {
      type: Array,
      default() {
        return []
      }
    }
  },*/
  data: function() {
    return {
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
      ]
    }
  },
  template:
  `
    <div>
      <div v-for="element in elements" :element="element" :key="element.id">
        <a>{{element.id}}</a>
        <a>{{element.date}}</a>
        <a>{{element.title}}</a>
        <button class="btn btn-primary">update</button>
        <button class="btn btn-primary">delete</button>
      </div>
    </div>
  `
}

new Vue({
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