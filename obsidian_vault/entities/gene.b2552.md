---
entity_id: "gene.b2552"
entity_type: "gene"
name: "hmp"
source_database: "NCBI RefSeq"
source_id: "gene-b2552"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2552"
  - "hmp"
---

# hmp

`gene.b2552`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2552`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hmp (gene.b2552) is a gene entity. It encodes hmp (protein.P24232). Encoded protein function: FUNCTION: Is involved in NO detoxification in an aerobic process, termed nitric oxide dioxygenase (NOD) reaction that utilizes O(2) and NAD(P)H to convert NO to nitrate, which protects the bacterium from various noxious nitrogen compounds. Therefore, plays a central role in the inducible response to nitrosative stress.; FUNCTION: In the presence of oxygen and NADH, HMP has NADH oxidase activity, which leads to the generation of superoxide and H(2)O(2), both in vitro and in vivo, and it has been suggested that HMP might act as an amplifier of superoxide stress. Under anaerobic conditions, HMP also exhibits nitric oxide reductase and FAD reductase activities. However, all these reactions are much lower than NOD activity.; FUNCTION: Various electron acceptors are also reduced by HMP in vitro, including dihydropterine, ferrisiderophores, ferric citrate, cytochrome c, nitrite, S-nitrosoglutathione, and alkylhydroperoxides. However, it is unknown if these reactions are of any biological significance in vivo. EcoCyc product frame: EG10456-MONOMER. EcoCyc synonyms: fsrB, hmpA. Genomic coordinates: 2685835-2687025...

## Biological Role

Repressed by sdsN (gene.b4719), fnr (protein.P0A9E5). Activated by metR (protein.P0A9F9), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24232|protein.P24232]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9F9|protein.P0A9F9]] `RegulonDB` `C` - regulator=MetR; target=hmp; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=hmp; function=+
- `represses` <-- [[gene.b4719|gene.b4719]] `RegulonDB` `S` - regulator=SdsN; target=hmp; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=hmp; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008396,ECOCYC:EG10456,GeneID:947018`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2685835-2687025:+; feature_type=gene
