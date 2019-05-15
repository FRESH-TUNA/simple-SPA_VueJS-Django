

var navTemplate = {
    template: 
    `
    <nav class="navbar navbar-expand-lg navbar-light">
            <a class="navbar-brand" href="">{{title}}</a>
                    <button type="button" class="btn btn-primary" v-on:click="mainview.currentView = 'main-template'">New Document</button>
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
