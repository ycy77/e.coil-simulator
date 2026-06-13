---
entity_id: "gene.b0972"
entity_type: "gene"
name: "hyaA"
source_database: "NCBI RefSeq"
source_id: "gene-b0972"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0972"
  - "hyaA"
---

# hyaA

`gene.b0972`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0972`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyaA (gene.b0972) is a gene entity. It encodes hyaA (protein.P69739). Encoded protein function: FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD1 is believed to have a role in hydrogen cycling during fermentative growth. EcoCyc product frame: HYAA-MONOMER. Genomic coordinates: 1032139-1033257. EcoCyc protein note: HyaA is the small subunit of hydrogenase 1. HyaA contains a distal [4Fe-4S]cluster, a medial [3Fe-4S] cluster and a unique proximal [4Fe-3S] cluster that is essential for oxygen tolerance (and see . The unique proximal [4Fe-3S] cluster is coordinated by six cysteine residues (at positions 17, 19, 20, 1115, 120 and 149 in the mature enzyme); the conserved cysteines at positions 19 and 120 correspond to glycine residues in standard oxygen-sensitive hydrogenases (hydrogenase 2 in E. coli K-12); a HyaA C19G mutation results in hydrogenase 1 enzyme that is devoid of H(2) oxidising activity in the presence of 1% oxygen . The reduction potential of the medial [3Fe-4S] cluster in oxygen tolerant hydrogenases is higher than in standard oxygen sensitive hydrogenases; a P242C mutation results in conversion of the [3Fe-4S] cluster to a [4Fe-4S] cluster and the modified enzyme is unable to sustain H(2) oxidation in the presence of 1% oxygen...

## Biological Role

Repressed by iscR (protein.P0AGK8). Activated by ydeO (protein.P76135).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69739|protein.P69739]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=hyaA; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=hyaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003286,ECOCYC:EG10468,GeneID:945579`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1032139-1033257:+; feature_type=gene
