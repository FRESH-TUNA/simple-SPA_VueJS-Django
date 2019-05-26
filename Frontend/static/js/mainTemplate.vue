<template>
    <div>
        <div v-for="element in currentViewData" :element="element" :key="element.id" class="post">
            <div class="postTitle">
                <h3>{{ element.title }}</h3>
                <a>{{ element.published_date }}</a>
            </div>
            <div>{{ element.content }}</div>
            <div class="postButtons">
                <button class="btn btn-primary" @click="mainview.showUpdateForm(element.id)">update</button>
                <button class="btn btn-primary" @click="mainview.deletePost(element.id)">delete</button>
            </div>
        </div>
    </div>
</template>

<script>
    module.exports = {
        props: ['currentViewData'],
        data: function () {
            return {
            }
        },
    }
</script>

<style scoped>
.post {
    width: 100%;
    border: 1px solid black;
    margin-top: 10px;
}
.postTitle {
    display: flex;
    justify-content: space-between;
}
.postButtons {
    display: flex;
    flex-direction: row-reverse;
}
</style>