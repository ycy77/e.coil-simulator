---
entity_id: "gene.b1597"
entity_type: "gene"
name: "asr"
source_database: "NCBI RefSeq"
source_id: "gene-b1597"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1597"
  - "asr"
---

# asr

`gene.b1597`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1597`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asr (gene.b1597) is a gene entity. It encodes asr (protein.P36560). Encoded protein function: FUNCTION: Required for growth and/or survival at acidic conditions (pH 4.5). Needed for the adaptation process at pH 4.5 that enables cells to survive at extremely low pH (pH 2.0). {ECO:0000269|PubMed:12670971}. EcoCyc product frame: G6855-MONOMER. Genomic coordinates: 1671376-1671684. EcoCyc protein note: Asr is a periplasmic, 'context-specific' chaperone that inhibits the aggregation of similarly charged clients and promotes the aggregation of oppositely charged clients. Asr is a highly charged, stress-induced, intrinsically disordered protein that contributes to the maintenance of outer membrane integrity under moderate acid stress . Asr plays a role in survival under acid conditions; it is involved in an acid-induced protective response that allows wild-type cells to survive incubation at very low pH . Asr also increases fitness in long-term stationary phase cultures in rich media and is important for colonization of the mouse intestine . Asr is post-translationally processed: the signal sequence is removed and the polypeptide is then cleaved into two pieces; only the C-terminal 8 kDa cleavage product can be detected. The cleavage sites have been characterized. The 8 kDa species appears to be the active species...

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5), rpoS (protein.P13445), rstA (protein.P52108), rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36560|protein.P36560]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=asr; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=asr; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=asr; function=+
- `activates` <-- [[protein.P52108|protein.P52108]] `RegulonDB` `S` - regulator=RstA; target=asr; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=asr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005337,ECOCYC:G6855,GeneID:945103`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1671376-1671684:+; feature_type=gene
