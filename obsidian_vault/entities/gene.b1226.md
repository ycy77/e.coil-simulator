---
entity_id: "gene.b1226"
entity_type: "gene"
name: "narJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1226"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1226"
  - "narJ"
---

# narJ

`gene.b1226`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1226`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narJ (gene.b1226) is a gene entity. It encodes narJ (protein.P0AF26). Encoded protein function: FUNCTION: Chaperone required for proper molybdenum cofactor insertion and final assembly of the membrane-bound respiratory nitrate reductase 1. Required for the insertion of the molybdenum into the apo-NarG subunit, maybe by keeping NarG in an appropriate competent-open conformation for the molybdenum cofactor insertion to occur. NarJ maintains the apoNarGH complex in a soluble state. Upon insertion of the molybdenum cofactor, NarJ seems to dissociate from the activated soluble NarGH complex, before its association with the NarI subunit on the membrane. {ECO:0000269|PubMed:16286471, ECO:0000269|PubMed:1732220, ECO:0000269|PubMed:9305880, ECO:0000269|PubMed:9632249}. EcoCyc product frame: NARJ-MONOMER. Genomic coordinates: 1285139-1285849. EcoCyc protein note: NarJ is part of the redox enzyme maturation protein (REMP) family of chaperones . NarJ acts as a private chaperone during the incorporation of the molybdenum cofactor into NarG, the α subunit of NITRATREDUCTA-CPLX , coordinating the final assembly and cofactor acquisition of nitrate reductase A. NarJ, encoded by the third gene in the narGHJI operon, is not part of the final nitrate reductase A enzyme, but is essential for nitrate reductase activity...

## Biological Role

Activated by fnr (protein.P0A9E5), narL (protein.P0AF28).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF26|protein.P0AF26]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=narJ; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=narJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004123,ECOCYC:EG10641,GeneID:945807`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1285139-1285849:+; feature_type=gene
