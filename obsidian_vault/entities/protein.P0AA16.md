---
entity_id: "protein.P0AA16"
entity_type: "protein"
name: "ompR"
source_database: "UniProt"
source_id: "P0AA16"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:3533941}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ompR kmt ompB b3405 JW3368"
---

# ompR

`protein.P0AA16`

## Static

- Type: `protein`
- Source: `UniProt:P0AA16`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:3533941}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system EnvZ/OmpR involved in osmoregulation (particularly of genes ompF and ompC) as well as other genes (PubMed:3010044, PubMed:3536870). Plays a central role in both acid and osmotic stress responses (PubMed:28526842, PubMed:30524381). Binds AT-rich DNA (PubMed:10633113). Binds to the promoter of both ompC and ompF; at low osmolarity it activates ompF transcription, while at high osmolarity it represses ompF and activates ompC transcription (PubMed:2403550, PubMed:2557454, PubMed:3023382, PubMed:3533941, PubMed:7592927). Involved in acid stress response; this requires EnvZ but not OmpR phosphorylation (PubMed:29138484). Phosphorylated by EnvZ; this stimulates OmpR's DNA-binding ability (PubMed:2558046, PubMed:2656684, PubMed:2668281, PubMed:2668953, PubMed:2674113, PubMed:7934854). Is also dephosphorylated by EnvZ (PubMed:2558046, PubMed:2668281, PubMed:7934854). A single OmpR protein can bind to DNA; OmpR dimers can form on the DNA in either direction, suggesting that interactions between the 2 DNA-binding domains are weak or absent (PubMed:18195018)...

## Biological Role

Component of DNA-binding transcriptional dual regulator OmpR (complex.ecocyc.CPLX0-8285), DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system EnvZ/OmpR involved in osmoregulation (particularly of genes ompF and ompC) as well as other genes (PubMed:3010044, PubMed:3536870). Plays a central role in both acid and osmotic stress responses (PubMed:28526842, PubMed:30524381). Binds AT-rich DNA (PubMed:10633113). Binds to the promoter of both ompC and ompF; at low osmolarity it activates ompF transcription, while at high osmolarity it represses ompF and activates ompC transcription (PubMed:2403550, PubMed:2557454, PubMed:3023382, PubMed:3533941, PubMed:7592927). Involved in acid stress response; this requires EnvZ but not OmpR phosphorylation (PubMed:29138484). Phosphorylated by EnvZ; this stimulates OmpR's DNA-binding ability (PubMed:2558046, PubMed:2656684, PubMed:2668281, PubMed:2668953, PubMed:2674113, PubMed:7934854). Is also dephosphorylated by EnvZ (PubMed:2558046, PubMed:2668281, PubMed:7934854). A single OmpR protein can bind to DNA; OmpR dimers can form on the DNA in either direction, suggesting that interactions between the 2 DNA-binding domains are weak or absent (PubMed:18195018). {ECO:0000269|PubMed:10633113, ECO:0000269|PubMed:18195018, ECO:0000269|PubMed:2403550, ECO:0000269|PubMed:2557454, ECO:0000269|PubMed:2558046, ECO:0000269|PubMed:2656684, ECO:0000269|PubMed:2668281, ECO:0000269|PubMed:2668953, ECO:0000269|PubMed:2674113, ECO:0000269|PubMed:28526842, ECO:0000269|PubMed:29138484, ECO:0000269|PubMed:3010044, ECO:0000269|PubMed:3023382, ECO:0000269|PubMed:30524381, ECO:0000269|PubMed:3533941, ECO:0000269|PubMed:3536870, ECO:0000269|PubMed:7592927, ECO:0000269|PubMed:7934854}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (52)

- `activates` --> [[gene.b0113|gene.b0113]] `RegulonDB` `S` - regulator=OmpR; target=pdhR; function=+
- `activates` --> [[gene.b0221|gene.b0221]] `RegulonDB` `S` - regulator=OmpR; target=fadE; function=+
- `activates` --> [[gene.b0222|gene.b0222]] `RegulonDB` `S` - regulator=OmpR; target=gmhA; function=+
- `activates` --> [[gene.b0464|gene.b0464]] `RegulonDB` `S` - regulator=OmpR; target=acrR; function=+
- `activates` --> [[gene.b0813|gene.b0813]] `RegulonDB` `S` - regulator=OmpR; target=rhtA; function=+
- `activates` --> [[gene.b0814|gene.b0814]] `RegulonDB` `S` - regulator=OmpR; target=ompX; function=+
- `activates` --> [[gene.b0929|gene.b0929]] `RegulonDB` `C` - regulator=OmpR; target=ompF; function=-+
- `activates` --> [[gene.b1037|gene.b1037]] `RegulonDB` `C` - regulator=OmpR; target=csgG; function=+
- `activates` --> [[gene.b1038|gene.b1038]] `RegulonDB` `C` - regulator=OmpR; target=csgF; function=+
- `activates` --> [[gene.b1039|gene.b1039]] `RegulonDB` `C` - regulator=OmpR; target=csgE; function=+
- `activates` --> [[gene.b1040|gene.b1040]] `RegulonDB` `C` - regulator=OmpR; target=csgD; function=+
- `activates` --> [[gene.b1465|gene.b1465]] `RegulonDB` `S` - regulator=OmpR; target=narV; function=+
- `activates` --> [[gene.b1466|gene.b1466]] `RegulonDB` `S` - regulator=OmpR; target=narW; function=+
- `activates` --> [[gene.b1467|gene.b1467]] `RegulonDB` `S` - regulator=OmpR; target=narY; function=+
- `activates` --> [[gene.b1468|gene.b1468]] `RegulonDB` `S` - regulator=OmpR; target=narZ; function=+
- `activates` --> [[gene.b1469|gene.b1469]] `RegulonDB` `S` - regulator=OmpR; target=narU; function=+
- `activates` --> [[gene.b1634|gene.b1634]] `RegulonDB` `C` - regulator=OmpR; target=dtpA; function=+
- `activates` --> [[gene.b1857|gene.b1857]] `RegulonDB` `S` - regulator=OmpR; target=znuA; function=+
- `activates` --> [[gene.b2215|gene.b2215]] `RegulonDB` `C` - regulator=OmpR; target=ompC; function=+
- `activates` --> [[gene.b2777|gene.b2777]] `RegulonDB` `S` - regulator=OmpR; target=queE; function=+
- `activates` --> [[gene.b3035|gene.b3035]] `RegulonDB` `S` - regulator=OmpR; target=tolC; function=+
- `activates` --> [[gene.b3089|gene.b3089]] `RegulonDB` `S` - regulator=OmpR; target=sstT; function=+
- `activates` --> [[gene.b3364|gene.b3364]] `RegulonDB` `S` - regulator=OmpR; target=tsgA; function=+
- `activates` --> [[gene.b3408|gene.b3408]] `RegulonDB` `C` - regulator=OmpR; target=feoA; function=+
- `activates` --> [[gene.b3409|gene.b3409]] `RegulonDB` `C` - regulator=OmpR; target=feoB; function=+
- `activates` --> [[gene.b3410|gene.b3410]] `RegulonDB` `C` - regulator=OmpR; target=feoC; function=+
- `activates` --> [[gene.b4396|gene.b4396]] `RegulonDB` `S` - regulator=OmpR; target=rob; function=+
- `activates` --> [[gene.b4439|gene.b4439]] `RegulonDB` `C` - regulator=OmpR; target=micF; function=+
- `activates` --> [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmpR; target=omrA; function=+
- `activates` --> [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmpR; target=omrB; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8285|complex.ecocyc.CPLX0-8285]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0435|gene.b0435]] `RegulonDB` `S` - regulator=OmpR; target=bolA; function=-
- `represses` --> [[gene.b0692|gene.b0692]] `RegulonDB` `S` - regulator=OmpR; target=potE; function=-
- `represses` --> [[gene.b0693|gene.b0693]] `RegulonDB` `S` - regulator=OmpR; target=speF; function=-
- `represses` --> [[gene.b0929|gene.b0929]] `RegulonDB` `C` - regulator=OmpR; target=ompF; function=-+
- `represses` --> [[gene.b1021|gene.b1021]] `RegulonDB` `S` - regulator=OmpR; target=pgaD; function=-
- `represses` --> [[gene.b1022|gene.b1022]] `RegulonDB` `S` - regulator=OmpR; target=pgaC; function=-
- `represses` --> [[gene.b1023|gene.b1023]] `RegulonDB` `S` - regulator=OmpR; target=pgaB; function=-
- `represses` --> [[gene.b1024|gene.b1024]] `RegulonDB` `S` - regulator=OmpR; target=pgaA; function=-
- `represses` --> [[gene.b1677|gene.b1677]] `RegulonDB` `S` - regulator=OmpR; target=lpp; function=-
- `represses` --> [[gene.b1829|gene.b1829]] `RegulonDB` `S` - regulator=OmpR; target=htpX; function=-
- `represses` --> [[gene.b1843|gene.b1843]] `RegulonDB` `S` - regulator=OmpR; target=yobB; function=-
- `represses` --> [[gene.b1844|gene.b1844]] `RegulonDB` `S` - regulator=OmpR; target=exoX; function=-
- `represses` --> [[gene.b2276|gene.b2276]] `RegulonDB` `S` - regulator=OmpR; target=nuoN; function=-
- `represses` --> [[gene.b2943|gene.b2943]] `RegulonDB` `S` - regulator=OmpR; target=galP; function=-
- `represses` --> [[gene.b3088|gene.b3088]] `RegulonDB` `S` - regulator=OmpR; target=alx; function=-
- `represses` --> [[gene.b4034|gene.b4034]] `RegulonDB` `S` - regulator=OmpR; target=malE; function=-
- `represses` --> [[gene.b4131|gene.b4131]] `RegulonDB` `S` - regulator=OmpR; target=cadA; function=-
- `represses` --> [[gene.b4132|gene.b4132]] `RegulonDB` `S` - regulator=OmpR; target=cadB; function=-
- `represses` --> [[gene.b4133|gene.b4133]] `RegulonDB` `S` - regulator=OmpR; target=cadC; function=-
- `represses` --> [[gene.b4803|gene.b4803]] `RegulonDB` `S` - regulator=OmpR; target=speFL; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3405|gene.b3405]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA16`
- `KEGG:ecj:JW3368;eco:b3405;ecoc:C3026_18475;`
- `GeneID:947913;99707869;99864652;`
- `GO:GO:0000156; GO:0000160; GO:0000976; GO:0005829; GO:0006355; GO:0032993; GO:0045893`

## Notes

DNA-binding dual transcriptional regulator OmpR (Transcriptional regulatory protein OmpR)
