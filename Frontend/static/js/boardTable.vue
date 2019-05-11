Vue.component('boardhead',{
    template:
    `
    <tr>
        <th>번호</th>
        <th>날짜</th>
        <th>제목</th>
        <th colspan="2"></th>
    </tr>
    `
})

Vue.component('boardrow',{
    props: ['element'],
    template:
    `
    <tr>
        <td>{{element.id}}</td>
        <td>{{element.date}}</td>
        <td>{{element.title}}</td>
        <td> 
            <button class="btn btn-primary">update</button>
        </td>
        <td> 
            <button class="btn btn-primary">delete</button>
        </td>
    </tr>
    `
})

new Vue({
    el: '#boardTable',
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
            },
        ]
    }
});