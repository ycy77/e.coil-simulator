---
entity_id: "gene.b2568"
entity_type: "gene"
name: "lepB"
source_database: "NCBI RefSeq"
source_id: "gene-b2568"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2568"
  - "lepB"
---

# lepB

`gene.b2568`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2568`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lepB (gene.b2568) is a gene entity. It encodes lepB (protein.P00803). Encoded protein function: Signal peptidase I (SPase I) (EC 3.4.21.89) (Leader peptidase I) EcoCyc product frame: EG10530-MONOMER. EcoCyc synonyms: lep. Genomic coordinates: 2704335-2705309. EcoCyc protein note: Signal peptidase catalyzes the cleavage of the amino-terminal leader or signal peptide from membrane-tethered secretory pre-proteins . The action of signal peptidase releases the mature secretory protein into the periplasm and retains the signal peptide in the membrane where it is further degraded by the inner membrane protease EG12436-MONOMER "RseP". Signal peptidase cleaves pre-proteins translocated by both the general Sec-system and the twin-arginine translocation (Tat) system . Signal peptidase also cleaves the signal peptide from bacteriophage M13 procoat protein . Signal peptidase is required for import of the bacterial toxin, colicin D Signal peptidase has two N-terminal transmembrane segments separated by a small cytoplasmic domain and a large C-terminal catalytic domain that is located in the periplasm. The second transmembrane segment is believed to function as a non-cleavable signal sequence . A soluble form of leader peptidase which lacks residues 2-76 is catalytically active in vitro and has been crystallised on its own and in complex with inhibitors...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco03060` Protein export (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00803|protein.P00803]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lepB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008450,ECOCYC:EG10530,GeneID:947040`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2704335-2705309:-; feature_type=gene
