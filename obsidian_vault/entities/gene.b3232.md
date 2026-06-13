---
entity_id: "gene.b3232"
entity_type: "gene"
name: "zapE"
source_database: "NCBI RefSeq"
source_id: "gene-b3232"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3232"
  - "zapE"
---

# zapE

`gene.b3232`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3232`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zapE (gene.b3232) is a gene entity. It encodes zapE (protein.P64612). Encoded protein function: FUNCTION: Reduces the stability of FtsZ polymers in the presence of ATP. Required for cell division under low-oxygen conditions. Hydrolyzes ATP but not GTP. {ECO:0000255|HAMAP-Rule:MF_01919, ECO:0000269|PubMed:24595368}. EcoCyc product frame: G7680-MONOMER. EcoCyc synonyms: yhcM. Genomic coordinates: 3378870-3379997. EcoCyc protein note: ZapE is an ATPase that is recruited to the constricting Z-ring late in cell division. ZapE affects polymerization of FtsZ in vitro . A ZapE K48A mutant lacks ATPase activity. In vitro, both ZapE and ZapE K48A interact with FtsZ polymers; ZapE appears to enhance polymerization of FtsZ, but does not affect the GTPase activity of FtsZ. Phospholipid binding of ZapE is enhanced in the presence of ATP . A zapE deletion mutant has no growth defect under aerobic conditions, but shows a growth defect under anaerobic growth conditions. At elevated temperatures, a ΔzapE mutant is filamentous . detected a mild cell division defect of a ΔzapE mutant even under aerobic growth conditions, but no enhanced growth defect under stress conditions. A ΔzapE ΔminC double mutant has a slow growth phenotype at high temperatures that can be rescued by both wild-type ZapE and ZapE(K48A) . In a large-scale TraDIS screen, zapE appeared to be important in late-stage biofilms...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64612|protein.P64612]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010602,ECOCYC:G7680,GeneID:947821`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3378870-3379997:-; feature_type=gene
