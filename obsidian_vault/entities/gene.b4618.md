---
entity_id: "gene.b4618"
entity_type: "gene"
name: "tisB"
source_database: "NCBI RefSeq"
source_id: "gene-b4618"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4618"
  - "tisB"
---

# tisB

`gene.b4618`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4618`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tisB (gene.b4618) is a gene entity. It encodes tisB (protein.A5A627). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system (Probable) (PubMed:18761622). Overexpression causes cessation of growth, induces stress-response, a number of membrane protein genes, and leads to cell death (PubMed:15620655, PubMed:18710431, PubMed:18761622). Inhibits ATP synthesis, ATP levels drop drastically quickly after induction (PubMed:18761622, PubMed:24513967). Part of the programmed response to DNA damage; damage leads to increased accumulation of the protein which slows or stops bacterial growth, probably allowing DNA repair before cells continue to grow (PubMed:15620655, PubMed:18761622). {ECO:0000269|PubMed:15620655, ECO:0000269|PubMed:18710431, ECO:0000269|PubMed:18761622, ECO:0000269|PubMed:24513967, ECO:0000305|PubMed:18710431}. EcoCyc product frame: MONOMER0-1922. EcoCyc synonyms: ysdB. Genomic coordinates: 3853553-3853642. EcoCyc protein note: TisB is the toxic peptide of a Type I toxin-antitoxin (TA) system consisting of a toxic protein and a small RNA antitoxin encoded by G0-10201. The TisB/IstR TA system appears to be found only in the Enterobacter-Escherichia clade and may be a recent arrival to this clade within the Enterobacterales order . TisB is involved in the formation of persister cells, which show tolerance to multiple antibiotics...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), istR (gene.b4616), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A5A627|protein.A5A627]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4616|gene.b4616]] `RegulonDB` `S` - regulator=IstR-1; target=tisB; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=tisB; function=-

## External IDs

- `Dbxref:ECOCYC:G0-9962,GeneID:5061527`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3853553-3853642:+; feature_type=gene
