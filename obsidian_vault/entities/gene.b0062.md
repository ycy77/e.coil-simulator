---
entity_id: "gene.b0062"
entity_type: "gene"
name: "araA"
source_database: "NCBI RefSeq"
source_id: "gene-b0062"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0062"
  - "araA"
---

# araA

`gene.b0062`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0062`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araA (gene.b0062) is a gene entity. It encodes araA (protein.P08202). Encoded protein function: FUNCTION: Catalyzes the conversion of L-arabinose to L-ribulose. EcoCyc product frame: ARABISOM-MONOMER. Genomic coordinates: 66835-68337. EcoCyc protein note: L-arabinose isomerase catalyzes the first step in the degradation of L-arabinose, its isomerization to L-ribulose. A reaction mechanism was proposed by . In vitro, the enzyme can also catalyze the conversion of D-galactose to D-tagatose, which is used commercially as a low-calorie substitute for sucrose . Electron micrographs showed that the subunits of L-arabinose isomerase are arranged in a stack of two trimers . Crystal structures of the enzyme alone and with a bound Mn2+ ion have been solved; they confirm that the enzyme forms a dimer of trimers . Most studies of the enzyme and its genetics were done in E. coli B/r. Transcription of the araBAD operon is induced in the presence of L-arabinose by the transcription factor AraC . araBAD expression can also induced by L-lyxose . araA mutants can not utilize L-arabinose for growth .

## Biological Role

Repressed by araC (protein.P0A9E0). Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08202|protein.P08202]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araA; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araA; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=araA; function=+
- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0000221,ECOCYC:EG10052,GeneID:947511`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:66835-68337:-; feature_type=gene
