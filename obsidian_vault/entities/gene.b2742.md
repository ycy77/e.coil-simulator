---
entity_id: "gene.b2742"
entity_type: "gene"
name: "nlpD"
source_database: "NCBI RefSeq"
source_id: "gene-b2742"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2742"
  - "nlpD"
---

# nlpD

`gene.b2742`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2742`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nlpD (gene.b2742) is a gene entity. It encodes nlpD (protein.P0ADA3). Encoded protein function: FUNCTION: Activator of the cell wall hydrolase AmiC. Required for septal murein cleavage and daughter cell separation during cell division. {ECO:0000269|PubMed:19525345, ECO:0000269|PubMed:20300061}. EcoCyc product frame: EG12111-MONOMER. Genomic coordinates: 2867614-2868753. EcoCyc protein note: NlpD is a divisome associated, outer membrane lipoprotein which activates the peptidoglycan (PG) hydrolase G7458-MONOMER "AmiC" involved in septal splitting . An NlpD-Mcherry fusion protein localises to the septal ring division site; envC nlpD double null mutants show significant defects in cell separation resulting in very long chain formation due to a defect in septal peptidoglycan splitting . NlpD contains a lipoprotein signal sequence, a LysM (lysin motif) domain (associated with peptidoglycan binding ) and a LytM (lysostaphin/M23 peptidase) domain (also found in EG12297-MONOMER EnvC, G7484-MONOMER YgeR and EG10013-MONOMER MepM) . NlpD (and EnvC) contain a degenerate LytM domain (dLytM) which is missing metal-binding and catalytic residues conserved in active LytM metallopeptidases...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADA3|protein.P0ADA3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nlpD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009004,ECOCYC:EG12111,GeneID:947011`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2867614-2868753:-; feature_type=gene
