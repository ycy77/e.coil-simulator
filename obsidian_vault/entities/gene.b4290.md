---
entity_id: "gene.b4290"
entity_type: "gene"
name: "fecB"
source_database: "NCBI RefSeq"
source_id: "gene-b4290"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4290"
  - "fecB"
---

# fecB

`gene.b4290`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4290`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fecB (gene.b4290) is a gene entity. It encodes fecB (protein.P15028). Encoded protein function: FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:17660286, PubMed:2651410). Binds both iron-free and iron-loaded citrate although it binds iron-loaded citrate with a higher affinity (PubMed:26600288). Binds different forms of Fe(3+)-citrate as well as citrate complexed with various representative Fe(3+)-mimics (Ga(3+), Al(3+), Sc(3+) and In(3+)) and a representative divalent metal ion (Mg(2+)) (PubMed:26600288). Can also bind various tricarboxylates in iron-free and iron-loaded form (PubMed:26600288). {ECO:0000269|PubMed:17660286, ECO:0000269|PubMed:2651410, ECO:0000269|PubMed:26600288}. EcoCyc product frame: FECB-MONOMER. Genomic coordinates: 4513406-4514308. EcoCyc protein note: fecB encodes the periplasmic substrate binding component of the iron dicitrate ABC transporter. FecB is a Class III periplasmic binding protein - it is predicted to be a bilobal protein with a single α-helical hinge connecting the two lobes . Purified FecB binds both iron-free and iron-loaded citrate at pH 5...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by fecI (protein.P23484).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15028|protein.P15028]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P23484|protein.P23484]] `RegulonDB` `C` - sigma=sigma19; target=fecB; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fecB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014065,ECOCYC:EG10287,GeneID:946838`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4513406-4514308:-; feature_type=gene
