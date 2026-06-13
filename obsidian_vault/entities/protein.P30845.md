---
entity_id: "protein.P30845"
entity_type: "protein"
name: "eptA"
source_database: "UniProt"
source_id: "P30845"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eptA pmrC yjdB b4114 JW5730"
---

# eptA

`protein.P30845`

## Static

- Type: `protein`
- Source: `UniProt:P30845`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the lipid A. The phosphoethanolamine modification is required for resistance to polymyxin. {ECO:0000250|UniProtKB:A0A0H3JML2}. EptA catalyses the addition of PHOSPHORYL-ETHANOLAMINE (pEtN) to the glucosamine disaccharide of lipid A core oligosaccharide. This modification promotes resistance to Polymyxins "polymyxin antibiotics" and antimicrobial peptides. L-1-PHOSPHATIDYL-ETHANOLAMINE Phosphatidylethanolamine serves as the donor and transfer occurs to the 1-phosphate and/or 4'-phosphate position; the reaction occurs on the outer surface of the inner membrane . A side product of the reaction is DIACYLGLYCEROL "1,2-diacyl-sn-glycerol" (DAG), a potential inhibitor of EptA . However, the DAG that is produced in converted rapidly to L-PHOSPHATIDATE phosphatidate by DIACYLGLYKIN-CPLX . Modification of E. coli LPS with pEtN is induced in cells grown under mild acidic conditions and in cells grown in LB with ammonium metavanadate (NH4VO3) . eptA transcript levels are increased under growth conditions with low Mg2+ concentrations, but these expression levels are decreased significantly in the pmrD mutant strain compared with the wild-type strain . The EptA (formerly YjdB) protein can be found in the membrane in a complex with ZipA and an unidentified 24 kDa protein . Related review:

## Biological Role

Catalyzes RXN-14379 (reaction.ecocyc.RXN-14379).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the lipid A. The phosphoethanolamine modification is required for resistance to polymyxin. {ECO:0000250|UniProtKB:A0A0H3JML2}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14379|reaction.ecocyc.RXN-14379]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4114|gene.b4114]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30845`
- `KEGG:ecj:JW5730;eco:b4114;ecoc:C3026_22230;`
- `GeneID:75169632;948629;`
- `GO:GO:0005886; GO:0009103; GO:0009244; GO:0009245; GO:0016776; GO:0046677`
- `EC:2.7.-.-`

## Notes

Phosphoethanolamine transferase EptA (EC 2.7.-.-) (Polymyxin resistance protein PmrC)
