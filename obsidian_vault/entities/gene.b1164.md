---
entity_id: "gene.b1164"
entity_type: "gene"
name: "ycgZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1164"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1164"
  - "ycgZ"
---

# ycgZ

`gene.b1164`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1164`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgZ (gene.b1164) is a gene entity. It encodes ycgZ (protein.P75991). Encoded protein function: FUNCTION: Probably a connector protein for RcsB/C regulation of biofilm formation, providing additional signal input into the two-component signaling pathway. Partially antagonizes the activities of YmgA and AriR, proteins that, via the Rcs phosphorelay, promote the synthesis of colanic acid, an exopolysaccharide and matrix component. EcoCyc product frame: G6604-MONOMER. Genomic coordinates: 1215789-1216025. EcoCyc protein note: Overexpression of ycgZ increases fitness as well as resistance to several antibiotics, including aztreonam and cefuroxime and decreases transcription of ompF . YcgZ appears to partially antagonize the effect of YmgA and AriR on mucoidy and curli expression . YcgZ is a substrate of the Lon protease . Temperature-dependent expression of ycgZ is regulated by the repressor BluR and the alternative sigma factor RpoS as well as by MarA . ycgZ is a member of the cold shock stimulon . yhdV was in the top 20 genes with increased translation in response to extreme acid stress (pH 4.4 compared to pH 7.6) as measured by ribosome coverage of its transcripts using RNA-Seq .

## Biological Role

Repressed by bluR (protein.P75989). Activated by rpoD (protein.P00579), marA (protein.P0ACH5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75991|protein.P75991]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ycgZ; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=ycgZ; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ycgZ; function=+
- `represses` <-- [[protein.P75989|protein.P75989]] `RegulonDB` `C` - regulator=BluR; target=ycgZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003907,ECOCYC:G6604,GeneID:945885`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1215789-1216025:+; feature_type=gene
