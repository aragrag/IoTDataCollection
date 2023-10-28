import React from 'react';
import { useTable, useSortBy, usePagination } from 'react-table';
import 'bootstrap/dist/css/bootstrap.min.css';
import './IoTDataTable.css';

function IoTDataTable({ data }) {
  const columns = React.useMemo(
    () => [
      {
        Header: 'Date',
        accessor: 'timestamp',
      },        
      {
        Header: 'Température (°C)',
        accessor: 'temperature',
      },
      {
        Header: 'Humidité (%)',
        accessor: 'humidity',
      },
    ],
    []
  );

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    prepareRow,
    page,
    canPreviousPage,
    canNextPage,
    pageOptions,
    pageCount,
    gotoPage,
    nextPage,
    previousPage,
    setPageSize,
    state: { pageIndex, pageSize },
  } = useTable(
    {
      columns,
      data,
    },
    useSortBy,
    usePagination
  );

  return (
    <section className="intro">
      <div className="gradient-custom-2 h-100">
        <div className="mask d-flex align-items-center h-100">
          <div className="container">
            <div className="row justify-content-center">
              <div className="col-12">
                <div className="table-responsive">
                  <table {...getTableProps()} className="table table-dark table-bordered mb-0">
                    <thead>
                      {headerGroups.map(headerGroup => (
                        <tr {...headerGroup.getHeaderGroupProps()}>
                          {headerGroup.headers.map(column => (
                            <th {...column.getHeaderProps(column.getSortByToggleProps())}>
                              {column.render('Header')}
                            </th>
                          ))}
                        </tr>
                      ))}
                    </thead>
                    <tbody {...getTableBodyProps()}>
                      {page.map(row => {
                        prepareRow(row);
                        return (
                          <tr {...row.getRowProps()}>
                            {row.cells.map(cell => {
                              return (
                                <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                              );
                            })}
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    <div className="pagination">
    <button className="btn btn-sm btn btn-dark" onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
        {'<<'}
    </button>{' '}
    <button className="btn btn-sm btn btn-primary" onClick={() => previousPage()} disabled={!canPreviousPage}>
        {'<'}
    </button>{' '}
    <span className="page-number">
        Page{' '}
        <strong>
        {pageIndex + 1} de {pageOptions.length}
        </strong>{' '}
    </span>
    <button className="btn btn-sm btn btn-primary" onClick={() => nextPage()} disabled={!canNextPage}>
        {'>'}
    </button>{' '}
    <button className="btn btn-sm btn btn-dark" onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
        {'>>'}
    </button>{' '}
    <div className="form-group" style={{ marginLeft: 'auto' }}>
        <select
        className="form-select form-select-sm"
        value={pageSize}
        onChange={e => {
            setPageSize(Number(e.target.value));
        }}
        >
        {[10, 20, 30, 40, 50].map(pageSize => (
            <option key={pageSize} value={pageSize}>
            Afficher {pageSize} éléments
            </option>
        ))}
        </select>
    </div>
    </div>

    </section>
  );
}

export default IoTDataTable;
