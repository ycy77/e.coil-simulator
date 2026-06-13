---
entity_id: "gene.b3157"
entity_type: "gene"
name: "ubiT"
source_database: "NCBI RefSeq"
source_id: "gene-b3157"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3157"
  - "ubiT"
---

# ubiT

`gene.b3157`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3157`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiT (gene.b3157) is a gene entity. It encodes ubiT (protein.P64599). Encoded protein function: FUNCTION: Required for oxygen-independent ubiquinone (coenzyme Q) biosynthesis (PubMed:31289180). Likely functions as an accessory factor (PubMed:31289180). Plays a key role in both anaerobiosis and aerobiosis conditions, allowing a smooth transition between the two conditions (PubMed:37283518). {ECO:0000269|PubMed:31289180, ECO:0000269|PubMed:37283518}. EcoCyc product frame: G7651-MONOMER. EcoCyc synonyms: yhbT. Genomic coordinates: 3300752-3301276. EcoCyc protein note: UbiT, like EG11474-MONOMER UbiJ, is an SCP2 domain-containing protein. It may similarly function as an accessory factor in the oxygen-independent pathway for ubiquinone biosynthesis . UbiT is a cytoplasmic protein that is expressed in early exponential phase and is degraded by the essential membrane-bound protease EG11506-MONOMER FtsH . A ΔubiT mutant is deficient in ubiquinone-8 biosynthesis under anaerobic growth conditions . Expression of ubiT is repressed by the biofilm regulator CsgD . UbiT: "ubiquinone biosynthesis T"

## Biological Role

Repressed by csgD (protein.P52106), nac (protein.Q47005).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64599|protein.P64599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=ubiT; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ubiT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010375,ECOCYC:G7651,GeneID:947669`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3300752-3301276:-; feature_type=gene
