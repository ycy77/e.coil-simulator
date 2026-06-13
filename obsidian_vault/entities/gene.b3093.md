---
entity_id: "gene.b3093"
entity_type: "gene"
name: "exuT"
source_database: "NCBI RefSeq"
source_id: "gene-b3093"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3093"
  - "exuT"
---

# exuT

`gene.b3093`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3093`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

exuT (gene.b3093) is a gene entity. It encodes exuT (protein.P0AA78). Encoded protein function: FUNCTION: Transport of aldohexuronates such as D-glucuronate and D-galacturonate (PubMed:6343797, PubMed:783117). Under anaerobic conditions, can play a critical role as a D-glucose transporter in the absence of sugar-PTS system (PubMed:32038601). {ECO:0000269|PubMed:32038601, ECO:0000269|PubMed:6343797, ECO:0000269|PubMed:783117}. EcoCyc product frame: EXUT-MONOMER. Genomic coordinates: 3245224-3246522. EcoCyc protein note: ExuT is a transporter for aldohexuronates such as D-galacturonate and D-glucuronate. Mutations affecting the transport of hexuronates have been shown to map to the exuT gene . ExuT is a member of the major facilitator superfamily (MFS) of transporters and probably functions as an aldohexuronate/proton symporter. The exuT gene constitutes a hexuronate-inducible single gene operon, whose expression is controlled by the ExuR regulator . Imported hexuronates are initially metabolised to 2-keto-3-deoxy-D-gluconate.

## Biological Role

Repressed by nac (protein.Q47005). Activated by dpiA (protein.P0AEF4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA78|protein.P0AA78]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=exuT; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=exuT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010171,ECOCYC:EG12738,GeneID:947601`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3245224-3246522:+; feature_type=gene
