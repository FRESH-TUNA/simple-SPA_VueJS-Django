

var navTemplate = {
    template: 
    `
    <nav class="navbar navbar-expand-lg navbar-light">
            <a class="navbar-brand" href="">{{title}}</a>
    </nav>
    `,
    data: function(){
        return {
            title: 'TunaBoard'
        }  
    }
}

var nav = new Vue({
    el: '#nav',
    components: {
        'nav-template': navTemplate
    }
})
