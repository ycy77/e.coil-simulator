---
entity_id: "gene.b4151"
entity_type: "gene"
name: "frdD"
source_database: "NCBI RefSeq"
source_id: "gene-b4151"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4151"
  - "frdD"
---

# frdD

`gene.b4151`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4151`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frdD (gene.b4151) is a gene entity. It encodes frdD (protein.P0A8Q3). Encoded protein function: FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used in anaerobic growth, and succinate dehydrogenase is used in aerobic growth. Anchors the catalytic components of the fumarate reductase complex to the cell inner membrane, binds quinones (PubMed:10373108). The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430}. EcoCyc product frame: FUM-MEMB2. Genomic coordinates: 4379007-4379366. EcoCyc protein note: This is one of two integral membrane proteins in the four subunit fumarate reductase complex . FrdC and FrdD each have three transmembrane helices connected by periplasmic loops; the N-terminus is located in the cytoplasm and the C-terminus is located in the periplasm...

## Biological Role

Repressed by narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), dcuR (protein.P0AD01), rpoS (protein.P13445).

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

- `encodes` --> [[protein.P0A8Q3|protein.P0A8Q3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=frdD; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=frdD; function=+
- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=frdD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=frdD; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=frdD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013595,ECOCYC:EG10333,GeneID:948668`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4379007-4379366:-; feature_type=gene
