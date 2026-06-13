---
entity_id: "gene.b3961"
entity_type: "gene"
name: "oxyR"
source_database: "NCBI RefSeq"
source_id: "gene-b3961"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3961"
  - "oxyR"
---

# oxyR

`gene.b3961`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3961`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oxyR (gene.b3961) is a gene entity. It encodes oxyR (protein.P0ACQ4). Encoded protein function: FUNCTION: Hydrogen peroxide (H2O2) sensor. Activates the expression of a regulon of H2O2-inducible genes such as katG, gor, ahpC, ahpF, oxyS (a regulatory RNA), dps, fur and grxA in response to H2O2. Represses transcription of phage Mu mom gene in a methylation-sensitive manner; MomR binds to the mom promoter when it is unmethylated but not if it is fully methylated (PubMed:2551682). Binds DNA in the upstream regions of its target genes; more than one site may be present per gene (PubMed:1864839, PubMed:2471187, PubMed:2551682). OxyR is inactivated by reduction of its essential disulfide bond by glutaredoxin (Grx1, grxA), itself positively regulated by OxyR (PubMed:9497290). Also has a positive regulatory effect on the production of surface proteins that control the colony morphology and auto-aggregation ability (PubMed:15659678). {ECO:0000269|PubMed:15659678, ECO:0000269|PubMed:1864839, ECO:0000269|PubMed:2551682, ECO:0000269|PubMed:9497290}. EcoCyc product frame: PD00214. EcoCyc synonyms: momR, mor. Genomic coordinates: 4158490-4159407. EcoCyc protein note: OxyR, "oxidative stress regulator," is the transcriptional dual regulator for the expression of antioxidant genes in response to oxidative stress, particularly, elevated levels of hydrogen peroxide...

## Biological Role

Repressed by oxyR (protein.P0ACQ4). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACQ4|protein.P0ACQ4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=oxyR; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=oxyR; function=+
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=oxyR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012973,ECOCYC:EG10681,GeneID:948462`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4158490-4159407:+; feature_type=gene
