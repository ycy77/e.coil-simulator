---
entity_id: "gene.b4154"
entity_type: "gene"
name: "frdA"
source_database: "NCBI RefSeq"
source_id: "gene-b4154"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4154"
  - "frdA"
---

# frdA

`gene.b4154`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4154`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frdA (gene.b4154) is a gene entity. It encodes frdA (protein.P00363). Encoded protein function: FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used during anaerobic growth, and succinate dehydrogenase is used during aerobic growth. The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430, ECO:0000269|PubMed:24374335}. EcoCyc product frame: FUM-FLAVO. Genomic coordinates: 4380510-4382318. EcoCyc protein note: FrdA is one of two catalytic subunits in the four subunit fumarate reductase complex. This subunit contains the FAD cofactor . This protein has similarity to the SdhA subunit of succinate dehydrogenase . A 2.2 Å crystal structure of L-aspartate oxidase suggests that an unusual tertiary structure is shared by L-aspartate oxidase, the SdhA subunit of succinate dehydrogenase, and the FrdA subunit of fumarate reductase...

## Biological Role

Repressed by lrp (protein.P0ACJ0), narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), dcuR (protein.P0AD01), rpoS (protein.P13445).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00363|protein.P00363]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=frdA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=frdA; function=+
- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=frdA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=frdA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=frdA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013604,ECOCYC:EG10330,GeneID:948667`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4380510-4382318:-; feature_type=gene
