---
entity_id: "protein.P0AEM6"
entity_type: "protein"
name: "fliA"
source_database: "UniProt"
source_id: "P0AEM6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00962}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliA flaD rpoF b1922 JW1907"
---

# fliA

`protein.P0AEM6`

## Static

- Type: `protein`
- Source: `UniProt:P0AEM6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00962}.

## Enriched Summary

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor controls the expression of flagella-related genes. {ECO:0000255|HAMAP-Rule:MF_00962, ECO:0000269|PubMed:2644646, ECO:0000269|PubMed:3536871, ECO:0000269|PubMed:7590326, ECO:0000269|PubMed:8866483}. σ28 is a minor sigma factor that is responsible for initiation of transcription of a number of genes involved in motility and flagellar synthesis . σ28 competes with σ70 for APORNAP-CPLX, binding to it more tightly than σ70 . A distinguishing feature of σ28 promoters is a long -10 region (GCCGATAA); in addition, its upstream GC is highly conserved . Thus, σ28 not only uses extended -10 recognition but also requires three recognition regions, -35, extended -10, and -10, for successful utilization of the core σ28 promoter . Both GC and the CG motifs are functionally important in the -10 region of σ28, and this is a composite element. Based on mutational and biochemical analyses, it was shown that the upstream GC constitutes an extended -10 motif and is recognized by R91 (which recognizes both 14G and 13C), a residue in domain 3 of σ28. The downstream CG is the upstream edge of the -10 region of the promoter; two residues in region 2...

## Biological Role

Component of RNA polymerase sigma 28 (complex.ecocyc.CPLX0-222).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor controls the expression of flagella-related genes. {ECO:0000255|HAMAP-Rule:MF_00962, ECO:0000269|PubMed:2644646, ECO:0000269|PubMed:3536871, ECO:0000269|PubMed:7590326, ECO:0000269|PubMed:8866483}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (26)

- `activates` --> [[gene.b1421|gene.b1421]] `RegulonDB` `S` - sigma=sigma28; target=trg; function=+
- `activates` --> [[gene.b1742|gene.b1742]] `RegulonDB` `S` - sigma=sigma28; target=ves; function=+
- `activates` --> [[gene.b1881|gene.b1881]] `RegulonDB` `S` - sigma=sigma28; target=cheZ; function=+
- `activates` --> [[gene.b1882|gene.b1882]] `RegulonDB` `S` - sigma=sigma28; target=cheY; function=+
- `activates` --> [[gene.b1883|gene.b1883]] `RegulonDB` `S` - sigma=sigma28; target=cheB; function=+
- `activates` --> [[gene.b1884|gene.b1884]] `RegulonDB` `S` - sigma=sigma28; target=cheR; function=+
- `activates` --> [[gene.b1885|gene.b1885]] `RegulonDB` `S` - sigma=sigma28; target=tap; function=+
- `activates` --> [[gene.b1886|gene.b1886]] `RegulonDB` `S` - sigma=sigma28; target=tar; function=+
- `activates` --> [[gene.b1920|gene.b1920]] `RegulonDB` `S` - sigma=sigma28; target=tcyJ; function=+
- `activates` --> [[gene.b1921|gene.b1921]] `RegulonDB` `S` - sigma=sigma28; target=fliZ; function=+
- `activates` --> [[gene.b1922|gene.b1922]] `RegulonDB` `S` - sigma=sigma28; target=fliA; function=+
- `activates` --> [[gene.b1923|gene.b1923]] `RegulonDB` `S` - sigma=sigma28; target=fliC; function=+
- `activates` --> [[gene.b1924|gene.b1924]] `RegulonDB` `S` - sigma=sigma28; target=fliD; function=+
- `activates` --> [[gene.b1925|gene.b1925]] `RegulonDB` `S` - sigma=sigma28; target=fliS; function=+
- `activates` --> [[gene.b1926|gene.b1926]] `RegulonDB` `S` - sigma=sigma28; target=fliT; function=+
- `activates` --> [[gene.b1944|gene.b1944]] `RegulonDB` `S` - sigma=sigma28; target=fliL; function=+
- `activates` --> [[gene.b1945|gene.b1945]] `RegulonDB` `S` - sigma=sigma28; target=fliM; function=+
- `activates` --> [[gene.b1946|gene.b1946]] `RegulonDB` `S` - sigma=sigma28; target=fliN; function=+
- `activates` --> [[gene.b1947|gene.b1947]] `RegulonDB` `S` - sigma=sigma28; target=fliO; function=+
- `activates` --> [[gene.b1948|gene.b1948]] `RegulonDB` `S` - sigma=sigma28; target=fliP; function=+
- `activates` --> [[gene.b1949|gene.b1949]] `RegulonDB` `S` - sigma=sigma28; target=fliQ; function=+
- `activates` --> [[gene.b1950|gene.b1950]] `RegulonDB` `S` - sigma=sigma28; target=fliR; function=+
- `activates` --> [[gene.b3072|gene.b3072]] `RegulonDB` `S` - sigma=sigma28; target=aer; function=+
- `activates` --> [[gene.b4355|gene.b4355]] `RegulonDB` `S` - sigma=sigma28; target=tsr; function=+
- `activates` --> [[gene.b4827|gene.b4827]] `RegulonDB` `S` - sigma=sigma28; target=fliX; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-222|complex.ecocyc.CPLX0-222]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1922|gene.b1922]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEM6`
- `KEGG:ecj:JW1907;eco:b1922;ecoc:C3026_10905;`
- `GeneID:93776231;948824;`
- `GO:GO:0000345; GO:0003677; GO:0003899; GO:0005829; GO:0006352; GO:0006355; GO:0016987; GO:0044780; GO:0071973; GO:2000142`

## Notes

RNA polymerase sigma factor FliA (RNA polymerase sigma factor for flagellar operon) (Sigma F) (Sigma-27) (Sigma-28)
