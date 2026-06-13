---
entity_id: "gene.b1926"
entity_type: "gene"
name: "fliT"
source_database: "NCBI RefSeq"
source_id: "gene-b1926"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1926"
  - "fliT"
---

# fliT

`gene.b1926`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1926`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliT (gene.b1926) is a gene entity. It encodes fliT (protein.P0ABY2). Encoded protein function: FUNCTION: Dual-function protein that regulates the transcription of class 2 flagellar operons and that also acts as an export chaperone for the filament-capping protein FliD. As a transcriptional regulator, acts as an anti-FlhDC factor; it directly binds FlhC, thus inhibiting the binding of the FlhC/FlhD complex to class 2 promoters, resulting in decreased expression of class 2 flagellar operons. As a chaperone, effects FliD transition to the membrane by preventing its premature polymerization, and by directing it to the export apparatus. {ECO:0000255|HAMAP-Rule:MF_01180}. EcoCyc product frame: EG11389-MONOMER. Genomic coordinates: 2005713-2006078. EcoCyc protein note: FliT is involved in flagellar motility . FliT function was primarily investigated in Salmonella typhimurium . FliT, along with FliS and FlgN, may function as cytoplasmic, substrate-specific chaperones of the flagellar export system. They share several similarities with other type III cytoplasmic chaperone family members . Affinity blot analysis showed that FliT binds in vitro to flagellar cap subunits (FliD) , suggesting that FliT may act as a chaperone which aids in the export and prevents premature aggregation of the FliD flagellar cap component...

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABY2|protein.P0ABY2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006411,ECOCYC:EG11389,GeneID:946433`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2005713-2006078:+; feature_type=gene
