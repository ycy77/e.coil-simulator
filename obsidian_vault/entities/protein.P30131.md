---
entity_id: "protein.P30131"
entity_type: "protein"
name: "hypF"
source_database: "UniProt"
source_id: "P30131"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hypF hydA b2712 JW5433"
---

# hypF

`protein.P30131`

## Static

- Type: `protein`
- Source: `UniProt:P30131`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the maturation of [NiFe] hydrogenases (PubMed:12377778, PubMed:12586941, PubMed:8661925). Along with HypE, it catalyzes the synthesis of the CN ligands of the active site iron of [NiFe]-hydrogenases (PubMed:12586941). HypF functions as a carbamoyl transferase using carbamoylphosphate as a substrate and transferring the carboxamido moiety in an ATP-dependent reaction to the thiolate of the C-terminal cysteine of HypE yielding a protein-S-carboxamide (PubMed:12586941, PubMed:15291820). In the absence of any other substrate, displays carbamoyl-phosphate phosphatase activity (PubMed:12377778). {ECO:0000269|PubMed:12377778, ECO:0000269|PubMed:12586941, ECO:0000269|PubMed:15291820, ECO:0000269|PubMed:8661925}. HypF is one of a number of proteins required for maturation of FORMHYDROGI-CPLX, FORMHYDROG2-CPLX and HYDROG3-CPLX . In the absence of other substrates, HypF hydrolyzes carbamoyl phosphate . However, under physiological conditions in the presence of EG10487-MONOMER HypE, HypF functions as a carbamoyl transferase, generating MONOMER0-4166 at the C-terminal cysteine residue of HypE . This reaction may involve the formation of a carbamoyladenylate intermediate . During the carbamoyl transfer reaction, HypE and HypF form a tight stochiometric complex ; the interaction has been characterized in detail...

## Biological Role

Catalyzes HypF carbamoyltransferase (reaction.ecocyc.RXN0-6435).

## Annotation

FUNCTION: Involved in the maturation of [NiFe] hydrogenases (PubMed:12377778, PubMed:12586941, PubMed:8661925). Along with HypE, it catalyzes the synthesis of the CN ligands of the active site iron of [NiFe]-hydrogenases (PubMed:12586941). HypF functions as a carbamoyl transferase using carbamoylphosphate as a substrate and transferring the carboxamido moiety in an ATP-dependent reaction to the thiolate of the C-terminal cysteine of HypE yielding a protein-S-carboxamide (PubMed:12586941, PubMed:15291820). In the absence of any other substrate, displays carbamoyl-phosphate phosphatase activity (PubMed:12377778). {ECO:0000269|PubMed:12377778, ECO:0000269|PubMed:12586941, ECO:0000269|PubMed:15291820, ECO:0000269|PubMed:8661925}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6435|reaction.ecocyc.RXN0-6435]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2712|gene.b2712]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30131`
- `KEGG:ecj:JW5433;eco:b2712;ecoc:C3026_14925;`
- `GeneID:944963;`
- `GO:GO:0003725; GO:0008270; GO:0016743; GO:0016874; GO:0051604; GO:0065003; GO:1904949`
- `EC:6.2.-.-`

## Notes

Carbamoyltransferase HypF (EC 6.2.-.-) (Carbamoyl phosphate-converting enzyme HypF) ([NiFe]-hydrogenase maturation factor HypF) (Hydrogenase maturation protein HypF)
