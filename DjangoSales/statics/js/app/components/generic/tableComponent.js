var tableComponent = {
	bindings: {
		data: '<dataTable',
		numberCount: '@'
	},
	controller: function(){
		console.log(this.data);
	},
	template:`
		<table class="table table-striped" id="example">
        <thead>
            <th ng-click="sort('upc')">UPC
                <span class="glyphicon sort-icon" ng-show="sortKey=='id'" ng-class="{'glyphicon-chevron-up':reverse,'glyphicon-chevron-down':!reverse}"></span>
            </th>
            <th ng-click="sort('proveedor.nombre')">Proveedor
                <span class="glyphicon sort-icon" ng-show="sortKey=='proveedor.nombre'" ng-class="{'glyphicon-chevron-up':reverse,'glyphicon-chevron-down':!reverse}"></span>
            </th>
            <th ng-click="sort('nombre')">Nombre
                <span class="glyphicon sort-icon" ng-show="sortKey=='nombre'" ng-class="{'glyphicon-chevron-up':reverse,'glyphicon-chevron-down':!reverse}"></span>
            </th>
            <th ng-click="sort('unidad')">Unidad
                <span class="glyphicon sort-icon" ng-show="sortKey=='unidad'" ng-class="{'glyphicon-chevron-up':reverse,'glyphicon-chevron-down':!reverse}"></span>
            </th>
            <th class="text-center">ACCIONES</th>
        </tr></thead>
        <tbody>
            <tr dir-paginate="x in productos|orderBy:sortKey:reverse|filter:search|itemsPerPage:10">
                <td>[[ x.upc ]]</td>
                <td>[[ x.proveedor.nombre ]]</td>
                <td>[[ x.nombre ]]</td>
                <td>[[ x.unidad.nombre ]]</td>

                <td class="text-center">
                    <a href="#" id="[[ x.id ]]" style="font-size:22px; color:#f0ad4e;" ng-click="detalleProducto(x)"><i class="fa fa-edit"></i></a>
                    <a href="#" data-id="[[ x.id ]]" style="font-size:22px; color:#d9534f; padding-left:10px;" data-producto="[[ x.nombre ]]"  ng-click="datosEliminar(x,$index)"><i class="fa fa-trash"></i></a>
                </td>
            </tr>
        </tbody>
    </table>
    <dir-pagination-controls
        max-size="5"
        direction-links="true"
        boundary-links="true" >
    </dir-pagination-controls>
	`
};

angular
	.module('app')
	.component('tableComponent', tableComponent);