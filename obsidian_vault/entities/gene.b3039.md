---
entity_id: "gene.b3039"
entity_type: "gene"
name: "ygiD"
source_database: "NCBI RefSeq"
source_id: "gene-b3039"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3039"
  - "ygiD"
---

# ygiD

`gene.b3039`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3039`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiD (gene.b3039) is a gene entity. It encodes ygiD (protein.P24197). Encoded protein function: FUNCTION: In vitro, opens the cyclic ring of dihydroxy-phenylalanine (DOPA) between carbons 4 and 5, thus producing an unstable seco-DOPA that rearranges nonenzymatically to betalamic acid. The physiological substrate is unknown. {ECO:0000269|PubMed:23666480}. EcoCyc product frame: EG11166-MONOMER. Genomic coordinates: 3181619-3182434. EcoCyc protein note: Purified YgiD has 4,5-DOPA dioxygenase activity. The physiological substrate of the enzyme is so far unknown . Expression of ygiD is induced by exposure to hydroquinone; this induction is abolished in a yhaJ mutant . In the E. coli asymptomatic bacteriuria (ABU) strains 83972 and VR50, YgiD is involved in biofilm formation in urine. ygiD expression is upregulated during growth in human urine compared to growth in minimal medium, and a ygiD mutant strains showed reduced biofilm formation in urine .

## Biological Role

Activated by yhaJ (protein.P67660).

## Enriched Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24197|protein.P24197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P67660|protein.P67660]] `RegulonDB` `S` - regulator=YhaJ; target=ygiD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009973,ECOCYC:EG11166,GeneID:946447`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3181619-3182434:-; feature_type=gene
