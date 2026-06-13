---
entity_id: "gene.b0070"
entity_type: "gene"
name: "setA"
source_database: "NCBI RefSeq"
source_id: "gene-b0070"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0070"
  - "setA"
---

# setA

`gene.b0070`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0070`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

setA (gene.b0070) is a gene entity. It encodes setA (protein.P31675). Encoded protein function: FUNCTION: Involved in the efflux of sugars. The physiological role may be the detoxification of non-metabolizable sugar analogs. Can transport IPTG, lactose and glucose. Has broad substrate specificity, with preferences for glucosides or galactosides with alkyl or aryl substituents. EcoCyc product frame: B0070-MONOMER. EcoCyc synonyms: yabM. Genomic coordinates: 77621-78799. EcoCyc protein note: SetA is an efflux transporter capable of exporting a number of sugars and sugar analogues; the physiological role of SetA is not clear. Overexpression of setA decreases the amount of protein produced form IPTG-responsive promoters and suppresses the growth inhibition that is associated with over-expression of membrane proteins; inside-out membrane vesicles prepared from cells overexpressing setA accumulate significant amounts of lactose in a manner that is sensitive to the proton ionophore, carbonyl cyanide m-chlorophenylhydrazone (CCCP) . SetA can transport lactose and glucose; SetA also transports some glucosides and galactosides with alkyl or aryl substituents and overexpression of setA protects cells from the toxic sugar analog 2-nitrophenyl-beta-D-thiogalactopyranoside (ONPTG)...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoD (protein.P00579), rpoS (protein.P13445), sgrR (protein.P33595).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31675|protein.P31675]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=setA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=setA; function=+
- `activates` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=setA; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=setA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000257,ECOCYC:EG11754,GeneID:944793`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:77621-78799:+; feature_type=gene
