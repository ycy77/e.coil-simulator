---
entity_id: "gene.b1991"
entity_type: "gene"
name: "cobT"
source_database: "NCBI RefSeq"
source_id: "gene-b1991"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1991"
  - "cobT"
---

# cobT

`gene.b1991`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1991`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cobT (gene.b1991) is a gene entity. It encodes cobT (protein.P36562). Encoded protein function: FUNCTION: Catalyzes the synthesis of alpha-ribazole-5'-phosphate from nicotinate mononucleotide (NAMN) and 5,6-dimethylbenzimidazole (DMB). EcoCyc product frame: DMBPPRIBOSYLTRANS-MONOMER. Genomic coordinates: 2063388-2064467. EcoCyc protein note: E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . cobT encodes a predicted dimethylbenzimidazole phosphoribosyltransferase. In addition to its predicted phosphoribosyltransferase activity, it is likely that CobT also participates directly in the synthesis of DMB . Expression of the cobUST operon is induced by cobinamide .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36562|protein.P36562]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cobT; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cobT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006611,ECOCYC:EG12151,GeneID:946517`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2063388-2064467:-; feature_type=gene
