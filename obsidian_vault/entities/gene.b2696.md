---
entity_id: "gene.b2696"
entity_type: "gene"
name: "csrA"
source_database: "NCBI RefSeq"
source_id: "gene-b2696"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2696"
  - "csrA"
---

# csrA

`gene.b2696`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2696`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csrA (gene.b2696) is a gene entity. It encodes csrA (protein.P69913). Encoded protein function: FUNCTION: A key translational regulator that binds mRNA to regulate translation initiation and/or mRNA stability, initially identified for its effects on central carbon metabolism (PubMed:8393005). Mediates global changes in gene expression, shifting from rapid growth to stress survival by linking envelope stress, the stringent response and the catabolite repression systems (PubMed:21488981, PubMed:28924029). Binds to the 5'-UTR of mRNA to repress or activate translation; 2 binding sites on the homodimer can bridge 2 sites within target RNA (By similarity). Exerts reciprocal effects on enzymes of gluconeogenesis and glycogen biosynthesis versus those of glycolysis (PubMed:16923806, PubMed:7493933). Negatively effects glycogen biosynthesis, gluconeogenesis, alters cell size and surface properties (PubMed:7493933, PubMed:7751274, PubMed:8393005). Activates regulates expression of glycolysis genes (PubMed:7493933). Represses biofilm formation (PubMed:11741870). Regulates glycogen synthesis under both aerobic and anaerobic conditions; overexpression strongly inhibits glycogen accumulation (PubMed:8393005). Binds to 4 sites in its own promoter, including the Shine-Dalgarno sequence, repressing its own translation; mutating the binding-sites decreases repression (PubMed:21696456)...

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69913|protein.P69913]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=csrA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=csrA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008866,ECOCYC:EG11447,GeneID:947176`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2818961-2819146:-; feature_type=gene
