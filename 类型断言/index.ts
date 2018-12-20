
declare var $:any;

let some:string|number;

function getSomeThing():string{
    return some as string;
    return <string>some;
}
$("xxx")
// function toBoolean(something:string|number):boolean{
//     let result:boolean;
//     try {
//         result = <boolean> something;
//     } catch (error) {
//         result = false;
//     }
//     return result;
// }