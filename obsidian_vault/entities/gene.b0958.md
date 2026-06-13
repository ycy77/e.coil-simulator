---
entity_id: "gene.b0958"
entity_type: "gene"
name: "sulA"
source_database: "NCBI RefSeq"
source_id: "gene-b0958"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0958"
  - "sulA"
---

# sulA

`gene.b0958`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0958`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sulA (gene.b0958) is a gene entity. It encodes sulA (protein.P0AFZ5). Encoded protein function: FUNCTION: Component of the SOS system and an inhibitor of cell division. Accumulation of SulA causes rapid cessation of cell division and the appearance of long, non-septate filaments. In the presence of GTP, binds a polymerization-competent form of FtsZ in a 1:1 ratio, thus inhibiting FtsZ polymerization and therefore preventing it from participating in the assembly of the Z ring. This mechanism prevents the premature segregation of damaged DNA to daughter cells during cell division. The effect of overexpression of SulA is neutralized by antitoxin CbeA (yeeU) (PubMed:22515815). {ECO:0000269|PubMed:10931335, ECO:0000269|PubMed:18245292, ECO:0000269|PubMed:2145263, ECO:0000269|PubMed:22515815, ECO:0000269|PubMed:6087326, ECO:0000269|PubMed:8432706, ECO:0000269|PubMed:9501185}. EcoCyc product frame: EG10984-MONOMER. EcoCyc synonyms: sfiA, suf. Genomic coordinates: 1020410-1020919. EcoCyc protein note: SulA inhibits cell division as part of the SOS response ; of the proteins induced during the SOS response, SulA is the most responsible for causing cell death . EG10347-MONOMER is the cellular target of SulA . SulA blocks Z ring formation by inhibiting polymerization of FtsZ . The SulA-FtsZ dissociation constant is 0...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), rcdA (protein.P75811). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFZ5|protein.P0AFZ5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=sulA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sulA; function=-
- `represses` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `C` - regulator=RcdA; target=sulA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003244,ECOCYC:EG10984,GeneID:947335`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1020410-1020919:-; feature_type=gene
