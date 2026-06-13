---
entity_id: "gene.b2808"
entity_type: "gene"
name: "gcvA"
source_database: "NCBI RefSeq"
source_id: "gene-b2808"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2808"
  - "gcvA"
---

# gcvA

`gene.b2808`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2808`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gcvA (gene.b2808) is a gene entity. It encodes gcvA (protein.P0A9F6). Encoded protein function: FUNCTION: Regulatory protein for the glycine cleavage system operon (gcv). Mediates activation of gcv by glycine and repression by purines. GcvA is negatively autoregulated. Binds to three sites upstream of the gcv promoter. EcoCyc product frame: PD00339. Genomic coordinates: 2941650-2942567. EcoCyc protein note: "Glycine cleavage A," GcvA, is a repressor of the glycine cleavage enzyme system, which is a secondary pathway for production of C1 units . It is negatively autoregulated, and it coordinately activates transcription of a small-RNA divergent gene . In the absence of glycine and the presence of GcvR, GcvA represses operons involved in the glycine cleavage system . GcvR is an accessory protein that binds directly to GcvA, bending DNA to form a repression complex (GcvA/GcvR) in the regulatory region of the gcvT operon . Glycine binds directly to GcvR to disrupt or block the association of the GcvA/GcvR complex, whereas purines appear to promote the formation of the repression complex through an unknown mechanism . GcvA also activates transcription of the gcv genes, via interaction with the α or σ subunits of RNA polymerase...

## Biological Role

Repressed by gcvA (protein.P0A9F6), glaR (protein.P37338).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9F6|protein.P0A9F6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvA; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gcvA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009202,ECOCYC:EG11795,GeneID:947278`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2941650-2942567:-; feature_type=gene
