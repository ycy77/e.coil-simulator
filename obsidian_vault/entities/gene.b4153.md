---
entity_id: "gene.b4153"
entity_type: "gene"
name: "frdB"
source_database: "NCBI RefSeq"
source_id: "gene-b4153"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4153"
  - "frdB"
---

# frdB

`gene.b4153`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4153`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frdB (gene.b4153) is a gene entity. It encodes frdB (protein.P0AC47). Encoded protein function: FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used during anaerobic growth, and succinate dehydrogenase is used during aerobic growth. The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430}. EcoCyc product frame: FUM-FE-S. Genomic coordinates: 4379783-4380517. EcoCyc protein note: This is one of two catalytic subunits of the four subunit fumarate reductase complex. FrdB contains 11 cysteine residues arranged in three clusters predicted to form the iron-sulfur clusters . This subunit contains three iron-sulfur clusters: a 4Fe-4S, a 3Fe-4S and a 2Fe-2S . This subunit has 38% identity to the succinate dehydrogenase iron-sulfur binding subunit, SdhB .

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

- `encodes` --> [[protein.P0AC47|protein.P0AC47]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=frdB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=frdB; function=+
- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=frdB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=frdB; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=frdB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013602,ECOCYC:EG10331,GeneID:948666`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4379783-4380517:-; feature_type=gene
