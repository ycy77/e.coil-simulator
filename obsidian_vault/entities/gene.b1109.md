---
entity_id: "gene.b1109"
entity_type: "gene"
name: "ndh"
source_database: "NCBI RefSeq"
source_id: "gene-b1109"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1109"
  - "ndh"
---

# ndh

`gene.b1109`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1109`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ndh (gene.b1109) is a gene entity. It encodes ndh (protein.P00393). Encoded protein function: FUNCTION: Alternative, nonproton pumping NADH:quinone oxidoreductase that delivers electrons to the respiratory chain by oxidation of NADH and reduction of quinones (PubMed:10664466, PubMed:2679883, PubMed:3122832, PubMed:6362717, PubMed:6784762, PubMed:7009604, PubMed:7020757). Utilizes NADH exclusively, and electron flow from NADH to ubiquinone does not generate an electrochemical gradient (PubMed:2679883, PubMed:3122832). {ECO:0000269|PubMed:10664466, ECO:0000269|PubMed:2679883, ECO:0000269|PubMed:3122832, ECO:0000269|PubMed:6362717, ECO:0000269|PubMed:6784762, ECO:0000269|PubMed:7009604, ECO:0000269|PubMed:7020757}.; FUNCTION: It may also contribute to copper homeostasis and bacterial oxidative protection (PubMed:10510271, PubMed:16759635, PubMed:21390523, PubMed:7487066). Shows cupric reductase activity, and catalyzes the reduction of Cu(2+) to Cu(+) with NADH as electron donor (PubMed:10510271). Exhibits Cu(2+) reductase activity in the presence of either FAD or quinone, but is unable to reduce Fe(3+) (PubMed:10510271). Contains thiolate-bound copper (PubMed:12176061). {ECO:0000269|PubMed:10510271, ECO:0000269|PubMed:12176061, ECO:0000269|PubMed:16759635, ECO:0000269|PubMed:21390523, ECO:0000269|PubMed:7487066}. EcoCyc product frame: NADH-DHII-MONOMER...

## Biological Role

Repressed by fis (protein.P0A6R3), fnr (protein.P0A9E5), arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by rpoD (protein.P00579), fis (protein.P0A6R3).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00393|protein.P00393]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ndh; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=ndh; function=-+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=ndh; function=-+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ndh; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=ndh; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=ndh; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003746,ECOCYC:EG10649,GeneID:946792`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1166085-1167389:+; feature_type=gene
