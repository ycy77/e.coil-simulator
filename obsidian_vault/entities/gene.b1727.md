---
entity_id: "gene.b1727"
entity_type: "gene"
name: "hxpB"
source_database: "NCBI RefSeq"
source_id: "gene-b1727"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1727"
  - "hxpB"
---

# hxpB

`gene.b1727`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1727`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hxpB (gene.b1727) is a gene entity. It encodes hxpB (protein.P77247). Encoded protein function: FUNCTION: Sugar-phosphate phosphohydrolase that catalyzes the dephosphorylation of D-mannitol 1-phosphate and D-sorbitol 6-phosphate (PubMed:27941785). Also catalyzes the dephosphorylation of 2-deoxyglucose 6-phosphate (2dGlu6P); this is a biologically important activity in vivo since it contributes to the elimination of this toxic compound and plays an important role in the resistance of E.coli to 2-deoxyglucose (PubMed:16990279). To a lesser extent, is also able to dephosphorylate mannose 6-phosphate (Man6P), erythrose-4-phosphate, 2-deoxyribose-5-phosphate (2dRib5P), ribose-5-phosphate (Rib5P) and glucose-6-phosphate (Glu6P) in vitro (PubMed:16990279). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:27941785}. EcoCyc product frame: G6932-MONOMER. EcoCyc synonyms: yniC. Genomic coordinates: 1809380-1810048. EcoCyc protein note: The hexitol phosphatase activity of HxpB was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . HxpB is a sugar phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. Its preferred substrate is 2-deoxyglucose-6-phosphate . The phosphatase activity of HxpB was first discovered in a high-throughput screen of purified proteins...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77247|protein.P77247]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hxpB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005761,ECOCYC:G6932,GeneID:945632`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1809380-1810048:+; feature_type=gene
