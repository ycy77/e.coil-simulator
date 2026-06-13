---
entity_id: "protein.P33195"
entity_type: "protein"
name: "gcvP"
source_database: "UniProt"
source_id: "P33195"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gcvP b2903 JW2871"
---

# gcvP

`protein.P33195`

## Static

- Type: `protein`
- Source: `UniProt:P33195`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. The P protein binds the alpha-amino group of glycine through its pyridoxal phosphate cofactor; CO(2) is released and the remaining methylamine moiety is then transferred to the lipoamide cofactor of the H protein. {ECO:0000255|HAMAP-Rule:MF_00711, ECO:0000269|PubMed:8375392}. Together with GcvH, GcvT and E3 (Lpd), GcvP forms a loosely associated complex known as the glycine cleavage system. GcvP, also known as the P-protein, catalyzes the decarboxylation of glycine. The remaining aminomethyl moiety is transferred to the lipoyl prosthetic group of the H-protein . Glycine cleavage system mutations cause a defect in utilization of glycine to form serine . Expression of the glycine cleavage enzyme system is induced by glycine , and the transcriptional regulation of the gcvTHP operon has been studied extensively. E. coli BW25113 strains with deletions in gcvP or EG11795 can grow in minimal media M9 when 0.5 M SARCOSINE is present but not in 0.75 M sarcosine . Review: Module 3.6.1.2

## Biological Role

Catalyzes glycine:lipoylprotein oxidoreductase (decarboxylating and acceptor-aminomethylating) (reaction.R03425). Component of glycine cleavage system (complex.ecocyc.GCVMULTI-CPLX), glycine decarboxylase (complex.ecocyc.GCVP-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. The P protein binds the alpha-amino group of glycine through its pyridoxal phosphate cofactor; CO(2) is released and the remaining methylamine moiety is then transferred to the lipoamide cofactor of the H protein. {ECO:0000255|HAMAP-Rule:MF_00711, ECO:0000269|PubMed:8375392}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R03425|reaction.R03425]] `KEGG` `database` - via EC:1.4.4.2
- `is_component_of` --> [[complex.ecocyc.GCVMULTI-CPLX|complex.ecocyc.GCVMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.GCVP-CPLX|complex.ecocyc.GCVP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2903|gene.b2903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33195`
- `KEGG:ecj:JW2871;eco:b2903;ecoc:C3026_15915;`
- `GeneID:947394;`
- `GO:GO:0004375; GO:0005829; GO:0005960; GO:0006730; GO:0016594; GO:0019464; GO:0030170; GO:0042802`
- `EC:1.4.4.2`

## Notes

Glycine dehydrogenase (decarboxylating) (EC 1.4.4.2) (Glycine cleavage system P-protein) (Glycine decarboxylase) (Glycine dehydrogenase (aminomethyl-transferring))
