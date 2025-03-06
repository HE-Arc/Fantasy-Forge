<!-- Component to add/substract certain parameters.

How to use:

<NumberInput :min = 5 :max = 10></NumberInput>
min nad max are optional, to define limits of the changer

<NumberInput
      v-for="item in fetchedItems"
      :key="item.id"
      :value="item.someValue"
    ></NumberInput>
-->

<template>
  <button
  class="value-control"
  onclick="numberInput.stepDown()"
  title="Decrease value"
  aria-label="Decrease value">-</button>

<input
  class="value-input"
  type="number"
  v-model="inputValue"
  name="numberInput"
  :min = "min"
  :max = "max"
  id="numberInput" readonly>

<button
  class="value-control"
  onclick="numberInput.stepUp()"
  title="Increase value"
  aria-label="Increase value">+</button>

</template>

<style scoped>

.value-control {
  margin: 0 0.1rem;
  padding: 0.5rem;
  background: transparent;
  border: 0.1rem solid #817474;;
  border-radius: 0.3rem;
  color: #6c5c5c;
  cursor: pointer;
}

.value-control:hover {
  background: #eee;
}

.value-control:active {
  background: #ddd;
}

.value-control:focus,
.value-input:focus {
  outline: 2px solid #b90606;
  outline-offset: 1px
}

.value-input {
  margin: 0;
  width: auto;
  border: 0.3rem double red;
  border-radius: 0.8rem;
  padding: 0.5rem;
  text-align: center;
}

.value-input:hover {
  border-color: #777;
}
</style>

<script>
export default {
  props: {
    min: {
      type: Number,
      default: 0, // Default min value
    },
    max: {
      type: Number,
      default: 10, // Default max value
    },
  },
  data() {
    return {
      inputValue: this.value,
    };
  },
  watch: {
    value(newVal) {
      this.inputValue = newVal;
    },
  },
};
</script>
