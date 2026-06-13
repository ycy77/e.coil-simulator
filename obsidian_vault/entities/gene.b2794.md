---
entity_id: "gene.b2794"
entity_type: "gene"
name: "queF"
source_database: "NCBI RefSeq"
source_id: "gene-b2794"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2794"
  - "queF"
---

# queF

`gene.b2794`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2794`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

queF (gene.b2794) is a gene entity. It encodes queF (protein.Q46920). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of 7-cyano-7-deazaguanine (preQ0) to 7-aminomethyl-7-deazaguanine (preQ1), a late step in the queuosine pathway. Is highly specific for its natural substrate preQ0, since it cannot use various aliphatic, aromatic, benzylic and heterocyclic nitriles, such as acetonitrile, benzonitrile, benzylcyanide and 2-cyanopyrrole, although it can reduce the substrate analog 5-cyanopyrrolo[2,3-d]pyrimidin-4-one with lesser efficiency. {ECO:0000269|PubMed:15767583, ECO:0000269|PubMed:23410922, ECO:0000269|PubMed:23595998}. EcoCyc product frame: G7452-MONOMER. EcoCyc synonyms: yqcD. Genomic coordinates: 2925348-2926196.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46920|protein.Q46920]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=queF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009162,ECOCYC:G7452,GeneID:947270`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2925348-2926196:+; feature_type=gene
