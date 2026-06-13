---
entity_id: "gene.b0497"
entity_type: "gene"
name: "rhsD"
source_database: "NCBI RefSeq"
source_id: "gene-b0497"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0497"
  - "rhsD"
---

# rhsD

`gene.b0497`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0497`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhsD (gene.b0497) is a gene entity. It encodes rhsD (protein.P16919). Encoded protein function: FUNCTION: Rhs elements have a nonessential function. They may play an important role in the natural ecology of the cell. EcoCyc product frame: EG10849-MONOMER. Genomic coordinates: 523261-527541. EcoCyc protein note: There are five homologous rhs loci that encode hydrophilic proteins with repetitive sequence elements and divergent C-termini . RhsA, RhsB, and RhsC define one subfamily, and RhsD and RhsE define a second subfamily of Rhs elements . Additional rhs elements and subfamilies have been characterized in other strains (not K-12) . Some of the rhs loci are reported to contain multiple open reading frames: rhsA , rhsB , and rhsC . RhsA, RhsB, RhsC, and RhsD include 28 copies of the core repeat element and RhsB, RhsC, and RhsE also include H-rpt (Hinc repeat) elements, which may be nonfunctional in RhsC . Overproduction of an RhsA fragment causes decreased survival at stationary phase; this effect is suppressed by co-overproduction of another part of the element and RpoS plays a role in moderation of toxicity . Regulation has been described . RhsD transcription is induced by sulfate starvation .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16919|protein.P16919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rhsD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001724,ECOCYC:EG10849,GeneID:945116`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:523261-527541:+; feature_type=gene
