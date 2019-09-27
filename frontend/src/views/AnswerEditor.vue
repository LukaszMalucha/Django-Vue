<template>
    <div class="container mt-2">
        <h1 class="mb-3">Edit Your Answer</h1>
        <form @submit.prevent="onSubmit">
            <textarea class="form-control" v-model="answerBody" rows="3">

            </textarea>
            <br>
            <button type="submit" class="btn btn-success">
                Publish your answer
            </button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>

</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
    name: "AnswerEditor",
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data(){
        return {
            questionSlug: null,
            answerBody: null,
            error: null
        }
    },
    methods: {
        onSubmit() {
            if (this.answerBody) {
                let endpoint = `/api/answers/${this.id}/`;
                apiService(endpoint, "PUT", { body: this.answerBody })
                .then(() => {
                    this.$router.push({
                        name: "question",
                        params: { slug: this.questionSlug }
                    })
                })
            } else {
                this.error = "Answer field can't be empty";
            }
        }
    },
    async beforeRouteEnter(to, from, next) {
        let endpoint = `/api/answers/${to.params.id}/`;
        let data = await apiService(endpoint);
//        to.params.previousAnswer = data.body;
//        to.params.questionSlug = data.question_slug;
        return next(vm => (
            vm.answerBody = data.body,
            vm.questionSlug = data.question_slug
        ));
    }
};
</script>