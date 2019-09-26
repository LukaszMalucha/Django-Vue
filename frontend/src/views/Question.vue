<template>
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{ question.content }}</h1>
            <p class="mb-0">Posted by:
              <span class="author-name">{{ question.author }}</span>
            </p>
            <p> {{ question.created_at }}</p>

        <hr>
        <div v-if="userHasAnswered">
            <p class="answer-added">
                You've written an answer!
            </p>
        </div>
        <div v-else-if="showForm">
            <form class="card">
                <div class="card-header px-3">
                    Answer the Question
                </div>
                <div class="card-block">
                    <textarea v-model="newAnswerBody" class="form-control" placeholder="Share Your Knowledge!" rows="5">

                    </textarea>
                </div>
                <div class="card-footer px-3">
                    <button type="submit" class="btn btn-sm btn-success">
                        Submit Your Answer
                    </button>
                </div>
            </form>
            <p v-if="error" class="error mt-2">{{ error }}</p>
        </div>
        <div v-else>
            <button class ="btn btn-sm btn-success" @click="showForm = true">
                Answer the Question
            </button>
        </div>
        <hr>
        </div>
        <div class="container">
            <AnswerComponent v-for="(answer, index) in answers"
             :answer="answer"
             :key="index"
            />
        </div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import AnswerComponent from "@/components/Answer.vue";
export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    components: {
        AnswerComponent
    },
    data() {
        return {
            question: {},
            answers: [],
            newAnswerBody: null,
            error: null,
            userHasAnswered: false,
            showForm: false
        }
    },
    methods: {
        setPageTitle(title) {
            document.title = title;
        },
        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint)
            .then(data => {
                this.question = data;
                this.userHasAnswered = data.user_has_answered;
                this.setPageTitle(data.content)
            })
        },
        getQuestionAnswers() {
            let endpoint = `/api/questions/${this.slug}/answers/`;
            apiService(endpoint)
            .then(data =>{
                this.answers = data.results;
            })
        }
    },
    created() {
        this.getQuestionData()
        this.getQuestionAnswers()
    }
}


</script>

<style scoped>
.author-name {
  font-weight: bold;
  color: #DC3545;
}

.answer-added {
    font-weight: bold;
    color: green;
}

.error {
    font-weight: bold;
    color: red;
}
</style>