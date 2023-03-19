import moment from 'moment';
console.log (moment.now());
const rigthNow=moment();
console.log (rigthNow);
const cumple=moment('2-4-1970','DD-MM-YYYY');
console.log (cumple.format('dddd'));
console.log (cumple.fromNow());