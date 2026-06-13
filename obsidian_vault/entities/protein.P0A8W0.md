---
entity_id: "protein.P0A8W0"
entity_type: "protein"
name: "nanR"
source_database: "UniProt"
source_id: "P0A8W0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanR yhcK b3226 JW3195"
---

# nanR

`protein.P0A8W0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8W0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional repressor that controls expression of the genes required for the catabolism of sialic acids (PubMed:12897000, PubMed:23935044, PubMed:9864311). Represses expression of the nanATEK-yhcH, nanCMS and yjhBC operons. Acts by binding directly to the Nan box, a region of approximately 30 bp covering the promoter region (PubMed:23935044). {ECO:0000269|PubMed:12897000, ECO:0000269|PubMed:23935044, ECO:0000269|PubMed:9864311}.

## Biological Role

Component of DNA-binding transcriptional dual regulator NanR (complex.ecocyc.CPLX0-8593).

## Annotation

FUNCTION: Transcriptional repressor that controls expression of the genes required for the catabolism of sialic acids (PubMed:12897000, PubMed:23935044, PubMed:9864311). Represses expression of the nanATEK-yhcH, nanCMS and yjhBC operons. Acts by binding directly to the Nan box, a region of approximately 30 bp covering the promoter region (PubMed:23935044). {ECO:0000269|PubMed:12897000, ECO:0000269|PubMed:23935044, ECO:0000269|PubMed:9864311}.

## Outgoing Edges (12)

- `activates` --> [[gene.b4312|gene.b4312]] `RegulonDB` `C` - regulator=NanR; target=fimB; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8593|complex.ecocyc.CPLX0-8593]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b3221|gene.b3221]] `RegulonDB` `C` - regulator=NanR; target=nanQ; function=-
- `represses` --> [[gene.b3222|gene.b3222]] `RegulonDB` `C` - regulator=NanR; target=nanK; function=-
- `represses` --> [[gene.b3223|gene.b3223]] `RegulonDB` `C` - regulator=NanR; target=nanE; function=-
- `represses` --> [[gene.b3224|gene.b3224]] `RegulonDB` `C` - regulator=NanR; target=nanT; function=-
- `represses` --> [[gene.b3225|gene.b3225]] `RegulonDB` `C` - regulator=NanR; target=nanA; function=-
- `represses` --> [[gene.b4279|gene.b4279]] `RegulonDB` `C` - regulator=NanR; target=nanX; function=-
- `represses` --> [[gene.b4280|gene.b4280]] `RegulonDB` `C` - regulator=NanR; target=nanY; function=-
- `represses` --> [[gene.b4309|gene.b4309]] `RegulonDB` `C` - regulator=NanR; target=nanS; function=-
- `represses` --> [[gene.b4310|gene.b4310]] `RegulonDB` `C` - regulator=NanR; target=nanM; function=-
- `represses` --> [[gene.b4311|gene.b4311]] `RegulonDB` `C` - regulator=NanR; target=nanC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3226|gene.b3226]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8W0`
- `KEGG:ecj:JW3195;eco:b3226;ecoc:C3026_17550;`
- `GeneID:75206076;945468;`
- `GO:GO:0000987; GO:0001046; GO:0001217; GO:0003677; GO:0003700; GO:0006351; GO:0006355; GO:0031334; GO:0042803; GO:2000143`

## Notes

HTH-type transcriptional repressor NanR
