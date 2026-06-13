---
entity_id: "gene.b1684"
entity_type: "gene"
name: "sufA"
source_database: "NCBI RefSeq"
source_id: "gene-b1684"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1684"
  - "sufA"
---

# sufA

`gene.b1684`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1684`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sufA (gene.b1684) is a gene entity. It encodes sufA (protein.P77667). Encoded protein function: FUNCTION: Member of gene cluster sufABCDSE that mediates iron-sulfur cluster assembly under oxidative stress and iron limitation conditions (PubMed:17941825). Binds [2Fe-2S] and [4Fe-4S] clusters by mobilizing sulfur atoms provided by the SufS-SufE cysteine desulfurase system and then transfers the assembled Fe-S clusters to target proteins including ferredoxin and aconitase (PubMed:17350000, PubMed:19366265). Seems to act as a Fe-S cluster carrier rather than a scaffold, this role being performed by SufB and SufC (PubMed:19810706, PubMed:23018275). {ECO:0000269|PubMed:17350000, ECO:0000269|PubMed:17941825, ECO:0000269|PubMed:19366265, ECO:0000269|PubMed:19810706, ECO:0000269|PubMed:23018275}. EcoCyc product frame: EG11378-MONOMER. EcoCyc synonyms: ydiC. Genomic coordinates: 1764018-1764386.

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77667|protein.P77667]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sufA; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=sufA; function=+
- `activates` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=sufA; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=sufA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005624,ECOCYC:EG11378,GeneID:949014`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1764018-1764386:-; feature_type=gene
