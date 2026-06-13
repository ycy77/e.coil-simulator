---
entity_id: "protein.P21645"
entity_type: "protein"
name: "lpxD"
source_database: "UniProt"
source_id: "P21645"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxD firA omsA b0179 JW0174"
---

# lpxD

`protein.P21645`

## Static

- Type: `protein`
- Source: `UniProt:P21645`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the N-acylation of UDP-3-O-(hydroxytetradecanoyl)glucosamine using 3-hydroxytetradecanoyl-ACP as the acyl donor. Is involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell. Prefers (3R)-3-hydroxytetradecanoyl-ACP over (3R)-3-hydroxyhexadecanoyl-ACP as the acyl donor in vitro, which is consistent with the structure of E.coli lipid A that contains over 95% (R)-3-hydroxytetradecanoate at the 2 and 2' positions. {ECO:0000269|PubMed:19655786, ECO:0000269|PubMed:8444173}.

## Biological Role

Component of UDP-3-O-(3-hydroxymyristoyl)glucosamine N-acyltransferase (complex.ecocyc.CPLX0-8016).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the N-acylation of UDP-3-O-(hydroxytetradecanoyl)glucosamine using 3-hydroxytetradecanoyl-ACP as the acyl donor. Is involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell. Prefers (3R)-3-hydroxytetradecanoyl-ACP over (3R)-3-hydroxyhexadecanoyl-ACP as the acyl donor in vitro, which is consistent with the structure of E.coli lipid A that contains over 95% (R)-3-hydroxytetradecanoate at the 2 and 2' positions. {ECO:0000269|PubMed:19655786, ECO:0000269|PubMed:8444173}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8016|complex.ecocyc.CPLX0-8016]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0179|gene.b0179]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21645`
- `KEGG:ecj:JW0174;eco:b0179;ecoc:C3026_00820;`
- `GeneID:86862689;944882;`
- `GO:GO:0005737; GO:0005829; GO:0009245; GO:0016020; GO:0016410; GO:0042802; GO:0046677; GO:0103118`
- `EC:2.3.1.191`

## Notes

UDP-3-O-(3-hydroxymyristoyl)glucosamine N-acyltransferase (UDP-3-O-(3-OHC14)-GlcN N-acyltransferase) (EC 2.3.1.191) (Protein FirA) (Rifampicin resistance protein) (UDP-3-O-(3-hydroxytetradecanoyl)glucosamine N-acyltransferase)
