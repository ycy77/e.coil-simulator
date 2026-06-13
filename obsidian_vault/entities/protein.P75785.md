---
entity_id: "protein.P75785"
entity_type: "protein"
name: "opgE"
source_database: "UniProt"
source_id: "P75785"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "opgE ybiP b0815 JW0800"
---

# opgE

`protein.P75785`

## Static

- Type: `protein`
- Source: `UniProt:P75785`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the osmoregulated periplasmic glucan (OPG) backbone. {ECO:0000269|PubMed:24228245}. OpgE is required for wild-type phosphoethanolamine modification of the branched periplasmic oligosaccharides known as CPD-16398 osmoregulated periplasmic glucans (OPG), formerly called membrane-derived oligosaccharides (MDO). OpgE is suggested to catalyse the transfer of a phosphoethanolamine group from phosphatidylethanolamine in the membrane to OPG in the periplasm. OPGs extracted from opgB- opgC- opgE- cells (opgB214::Tn10 opgC::Tn5 opgE2::cml) are not substituted with phosphoglycerol, succinyl nor phosphoethanolamine moieties. OPGs extracted from opgB- opgC- cells (opgB214::Tn10 opgC::Tn5) contain phosphoethanolamine substitutions but do not contain phosphoglycerol nor succinyl modifications . OpgE is predicted to contain 4 transmembrane segments plus a periplasmic domain with sulfuric ester hydrolase and transferase activity . Mutant strains lacking substituents do not have an observable phenotype .

## Biological Role

Catalyzes RXN-15210 (reaction.ecocyc.RXN-15210).

## Annotation

FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the osmoregulated periplasmic glucan (OPG) backbone. {ECO:0000269|PubMed:24228245}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-15210|reaction.ecocyc.RXN-15210]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0815|gene.b0815]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75785`
- `KEGG:ecj:JW0800;eco:b0815;ecoc:C3026_05130;`
- `GeneID:93776612;945360;`
- `GO:GO:0005886; GO:0009244; GO:0016776; GO:1900727`
- `EC:2.7.-.-`

## Notes

Phosphoethanolamine transferase OpgE (EC 2.7.-.-)
