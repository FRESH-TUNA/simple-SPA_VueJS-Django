var footerTemplate = {
    template: 
    `
    <div>{{footerTitle}}</div>
    `,
    data: function(){
        return {
            footerTitle: 'T U N A S T R E A M'
        }  
    }
}

var footer = new Vue({
    el: '#footer',
    components: {
        'footer-template': footerTemplate
    }
})
