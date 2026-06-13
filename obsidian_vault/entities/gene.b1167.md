---
entity_id: "gene.b1167"
entity_type: "gene"
name: "ymgC"
source_database: "NCBI RefSeq"
source_id: "gene-b1167"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1167"
  - "ymgC"
---

# ymgC

`gene.b1167`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1167`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymgC (gene.b1167) is a gene entity. It encodes ymgC (protein.P75994). Encoded protein function: Uncharacterized protein YmgC EcoCyc product frame: G6607-MONOMER. Genomic coordinates: 1216748-1216996. EcoCyc protein note: Deletion of ymgC increases biofilm formation and motility . Expression of ymgC is regulated under conditions of biofilm formation. Deletion of tqsA (encoding the AI-2 transporter) and the presence of AI-2 or the stationary phase biofilm signal indole repress ymgC expression. ymgC is repressed in young and mature biofilms, but is induced in the intermediate, developed biofilms and by rapid acid treatment . Expression of ymgC is regulated by the repressor BluR as well as by MarA and is increased under low temperature growth conditions .

## Biological Role

Repressed by bluR (protein.P75989). Activated by rpoD (protein.P00579), marA (protein.P0ACH5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75994|protein.P75994]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ymgC; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=ymgC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ymgC; function=+
- `represses` <-- [[protein.P75989|protein.P75989]] `RegulonDB` `C` - regulator=BluR; target=ymgC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003915,ECOCYC:G6607,GeneID:945090`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1216748-1216996:+; feature_type=gene
